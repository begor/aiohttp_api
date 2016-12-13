import asyncio
from aiohttp import web

import settings
import db


loop = asyncio.get_event_loop()
app = web.Application(loop=loop)


app['config'] = settings.load_settings()
print(app['config'])


app.on_startup.append(db.init_pg)
app.on_shutdown.append(db.close_pg)

web.run_app(app)
