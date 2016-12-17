from datetime import datetime
import db
import sqlalchemy as sa
from aiohttp import web

from helpers import json_response


class GenericView(web.View):
    def aquire_db(self):
        return self.request.app['db'].acquire()

    async def get_request_params(self):
        params = await self.request.json()
        time_ = datetime.now()
        params['updated_at'] = params['created_at'] = time_
        return params


class NoteView(GenericView):

    @property
    def note_id(self):
        return self.request.match_info['id']

    async def update_note(self, conn):
        params = await self.get_request_params()
        update = (db.note
                    .update()
                    .values(**params)
                    .where(db.note.c.id==self.note_id))
        result = await conn.execute(update)

    async def get_note(self, conn):
        cursor = await conn.execute(
            db.note.select(db.note.c.id==self.note_id))
        updated = await cursor.fetchone()
        return dict(updated)

    async def put(self):
        async with self.aquire_db() as conn:
            _ = await self.update_note(conn)
            updated = await self.get_note(conn)
        return json_response(data=updated)


class NoteCollectionView(GenericView):

    async def get(self):
        async with self.aquire_db() as conn:
            cursor = await conn.execute(db.note.select())
            records = await cursor.fetchall()
            notes = [dict(n) for n in records]
            return json_response(data={'notes': notes})

    async def post(self):
        params = await self.get_request_params()
        async with self.aquire_db() as conn:
            cursor = await conn.execute(db.note.insert(params))
        return json_response(data="ok")
