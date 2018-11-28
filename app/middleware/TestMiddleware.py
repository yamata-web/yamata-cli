from yamata.base.middleware import Middleware as BaseMiddleware


class TestMiddleware(BaseMiddleware):

    def handle(self, request, next_handle):
        print('hello test middleware')
        return next_handle
