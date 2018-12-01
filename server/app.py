from aiohttp import web
from server.routes import routes


app = web.Application()
app.add_routes([web.get('/', routes.ping),
                web.get('/{name}', routes.handle)])

web.run_app(app)