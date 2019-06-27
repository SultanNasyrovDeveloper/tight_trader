from settings import BASE_DIR


def setup_static_routes(app):
    app.router.add_static('/static/', path=BASE_DIR / 'static', name='static')

