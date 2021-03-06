import gevent
from gevent.pywsgi import (  # noqa: F401
    WSGIServer,
)
from gevent.queue import (  # noqa: F401
    JoinableQueue,
)
from gevent import (  # noqa; F401
    subprocess,
    socket,
)


sleep = gevent.sleep
spawn = gevent.spawn


class Timeout(gevent.Timeout):
    def check(self):
        pass


def make_server(host, port, application, *args, **kwargs):
    server = WSGIServer((host, port), application, *args, **kwargs)
    return server
