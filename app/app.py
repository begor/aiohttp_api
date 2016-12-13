import asyncio
from aiohttp import web

import settings

loop = asyncio.get_event_loop()
app = web.Application(loop=loop)

app['config'] = settings.load_settings()
print(app['config'])
