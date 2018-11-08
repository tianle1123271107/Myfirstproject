#由于我们的Web App建立在asyncio的基础上，因此用aiohttp写一个基本的app.py：
import logging;logging.basicConfig(level=logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')#配置logging基本的设置，然后在控制台输出日志
import asyncio,os,json,time
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>hello world<h1>',content_type='text/html')

async def init(loop):
    app=web.Application(loop=loop)
    app.router.add_route('get','/',index)
    srv=await loop.create_server(app.make_handler(),'127.0.0.1','9002')
    logging.info('server started at http://127.0.0.1:9002...')
    return srv

loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

