import os
import logger
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

log = logger.Logger('server')


class ServerHTTPRequestHandler(BaseHTTPRequestHandler, object):

    read_size = 1024 * 8

    def __init__(self, request, client_address, server):
        super(ServerHTTPRequestHandler, self).__init__(request, client_address, server)
        self.protocol_version = 'HTTP/1.1'

    def do_POST(self):
        length = long(self.headers.get('Content-Length'))
        path = self.headers.get('File-Path', '')
        size = self.read_size
        write_file = self.get_file_write(path)
        if write_file is None:
            self.error('File-Path not find from header')
            return 1
        try:
            while True:
                if length < self.read_size:
                    size = length
                read = self.rfile.read(size)
                write_file.write(read)
                length -= size
                if length == 0:
                    break
        except Exception as e:
            log.error('failed to save file. %s' % e)
            return 1
        finally:
            write_file.close()
        self.send_response(200)
        self.end_headers()

    def error(self, message, code=400):
        self.send_error(code, message=message)
        self.end_headers()

    def get_file_write(self, path):
        try:
            if path == '':
                log.error('File-Path is empty.')
                return None
            paths = os.path.split(path)
            if not os.path.exists(paths[0]):
                os.mkdir(paths[0])
            return open(path, 'w')
        except Exception as e:
            log.error('failed to create file. %s' % e)
            return None

    def do_GET(self):
        log.info(self.headers)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def log_message(self, formats, *args):
        log.info("%s - %s" % (self.client_address[0], formats % args))

    def log_error(self, formats, *args):
        log.error("%s - %s" % (self.client_address[0], formats % args))


def start_server():
    server = HTTPServer(('', 1234), ServerHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    start_server()
