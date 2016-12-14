from aiohttp import web

import models


async def notes_index(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(models.note.select())
        records = await cursor.fetchall()
        notes = [dict(n) for n in records]
        return web.json_response(data={'notes': notes})
