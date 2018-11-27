import logger
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

log = logger.Logger('server')


class ServerHTTPRequestHandler(BaseHTTPRequestHandler, object):

    def __init__(self, request, client_address, server):
        super(ServerHTTPRequestHandler, self).__init__(request, client_address, server)
        self.protocol_version = 'HTTP/1.1'

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write('')

    def log_message(self, formats, *args):
        log.info("%s - %s" % (self.client_address[0], formats % args))

    def log_error(self, formats, *args):
        log.error("%s - %s" % (self.client_address[0], formats % args))


def start_server():
    server = HTTPServer(('', 1234), ServerHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    start_server()
