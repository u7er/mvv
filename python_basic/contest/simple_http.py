from http.server import BaseHTTPRequestHandler,HTTPServer, SimpleHTTPRequestHandler
import time
import traceback

class GetHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            self.path = 'pages/index.html'
            return SimpleHTTPRequestHandler.do_GET(self)

        def do_POST(self):
            self.send_response(200)
            return

def goRest():
    global ordering

    Handler=GetHandler
    httpd=HTTPServer(("localhost", 50000), Handler)
    httpd.serve_forever()


goRest()