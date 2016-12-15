from datetime import datetime
import db
import sqlalchemy as sa
from aiohttp import web

from helpers import json_response


class NoteView(web.View):

    def __aquire_db(self):
        return self.request.app['db'].acquire()

    async def get_post_params(self):
        params = await self.request.json()
        time_ = datetime.now()
        params['updated_at'] = params['created_at'] = time_
        return params

    async def get(self):
        async with self.__aquire_db() as conn:
            cursor = await conn.execute(db.note.select())
            records = await cursor.fetchall()
            notes = [dict(n) for n in records]
            return json_response(data={'notes': notes})

    async def post(self):
        params = await self.get_post_params()
        async with self.__aquire_db() as conn:
            cursor = await conn.execute(db.note.insert(params))
        return web.json_response(data="ok")
