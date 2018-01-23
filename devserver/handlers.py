from django.core.handlers.wsgi import WSGIHandler

from devserver.middleware import DevServerMiddleware


class DevServerHandler(WSGIHandler):
    pass
