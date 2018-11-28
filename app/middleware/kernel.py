# -*- coding: utf-8 -*-
from .TestMiddleware import TestMiddleware


class HttpKernel(object):
    # global middleware
    middleware = [

    ]

    # groups middleware
    middleware_groups = {

    }

    # signal middleware
    route_middleware = {
        'test': TestMiddleware()
    }
