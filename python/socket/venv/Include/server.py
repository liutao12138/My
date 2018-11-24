import logger
import socket

log = logger.Logger('server', log=True)


class Server:
    server = None

    def __init__(self):
        self.server = socket.socket()
        self.server.bind(('127.0.0.1', 8788))
        self.server.listen(5)

    def listen(self):
        while True:
            conn, addr = self.server.accept()
            log.info(list(addr))
            log.info(conn.recv(1024))


if __name__ == '__main__':
    Server().listen()
