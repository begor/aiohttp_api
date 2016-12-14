import asyncio
from aiohttp import web

import settings
import db
import routes


loop = asyncio.get_event_loop()
app = web.Application(loop=loop)


app['config'] = settings.load_settings()

app.on_startup.append(db.init_pg)
app.on_shutdown.append(db.close_pg)

routes.setup_routes(app)

web.run_app(app)
