"""
AngularJS / Python backend

This script uses aiohttp for the backend. Make sure to have aiohttp installed,
then run `python app_aiohttp.py` from the directory this file is contained in.

This example utilizes the async/await syntax introduced by PEP 492 that is only 
valid for Python 3.5+. See https://docs.python.org/3/library/asyncio.html for 
alternatives on older platforms.
"""

from aiohttp import web
from functools import partial
import os

app = web.Application()

async def serve_file(directory, request):
    path = request.match_info.get('path')
    return web.FileResponse(os.path.join(directory, path))

serve_static = partial(serve_file, 'static')
serve_vendor = partial(serve_file, 'vendor')

async def serve_index(request):
    return web.FileResponse('static/index.html')

async def greet(request):
    name = request.match_info.get('name')
    return web.json_response({
        'message' : 'Hello {}'.format(name)
    })

# Routes handles by aiohttp. Note, any AngularJS local
# route should also be added here with handler 'serve_index'.
# Otherwise, calling the route directly will not allow AngularJS
# to handle it safely.
app.router.add_get('/', serve_index)
app.router.add_get('/static/{path:.*}', serve_static)
app.router.add_get('/vendor/{path:.*}', serve_vendor)
app.router.add_get('/api/greet/{name}', greet)

if __name__ == "__main__":
    web.run_app(app)