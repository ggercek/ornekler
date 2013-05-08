#!/usr/bin/env python
from gevent import monkey
from socketio.server import SocketIOServer
import django.core.handlers.wsgi
import os
import sys

monkey.patch_all()

try:
    from socketIO_Test import settings
except ImportError:
    sys.stderr.write("Error: Can't find the file 'settings.py'.")
    sys.exit(1)

PORT = 8000
os.environ['DJANGO_SETTINGS_MODULE'] = "socketIO_Test.settings"

application = django.core.handlers.wsgi.WSGIHandler()

if __name__ == "__main__":
    print 'Listening on http://127.0.0.1:%s and on port 843 (flash policy server)' % PORT
    SocketIOServer(('', PORT), application, resource="socket.io").serve_forever()
