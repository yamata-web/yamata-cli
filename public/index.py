# -*- coding: utf-8 -*-
from yamata.request.request import Request
from yamata.router.router import Router
from yamata.middleware.middleware_handler import MiddlewareHandler

is_init = False


def application(env, response):
    global is_init
    if is_init is False:
        init_data()
    request = Request(env)
    route, pattern_dict = Router.match(request.method, request.url)
    if route:
        result = MiddlewareHandler.handle_global_middleware(request)
        result = MiddlewareHandler.handle_middleware_for_route(request, route)
        request = result
    else:
        response('404 NotFound', [('Content-Type', 'text/html')])
        return [404]

    response('200 OK', [('Content-Type', 'text/html')])
    return ["Hello World"]


def init_data():
    print('init data')
    from app.middleware.kernel import HttpKernel
    import routes.api
    import routes.web
    MiddlewareHandler.init(
        HttpKernel.middleware,
        HttpKernel.middleware_groups,
        HttpKernel.route_middleware
    )
    global is_init
    is_init = True
