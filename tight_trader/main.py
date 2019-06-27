from aiohttp import web

import aiohttp_jinja2
import jinja2

from settings import BASE_DIR, config
from db import create_engine, close_engine
from routes import setup_static_routes, setup_routes

from tight_trader.trading_bot import setup_routes as trading_bot_routes_setup


# APPLICATION
# -----------
# create app
app = web.Application()
app['config'] = config

# add methods on startapp
app.on_startup.append(create_engine)
app.on_shutdown.append(close_engine)

# add static routes
setup_static_routes(app)

# add main routes
setup_routes(app)

# load jinja2
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(BASE_DIR / 'platform' / 'templates')))


# NESTED APPS
# -----------
trading_bot = web.Application()
trading_bot_routes_setup(trading_bot)


# REGISTER NESTED APPS
# --------------------

# RUN
# ---
web.run_app(app)