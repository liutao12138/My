import logging
import os


class Logger(logging.getLoggerClass(), object):

    def __init__(self, name, log=False, console=True, level=logging.INFO, path='/var/log/socket/log.log'):
        super(Logger, self).__init__(name, level)
        formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s %(filename)s %(funcName)s line%(lineno)d:%(message)s',
                                      datefmt='[%Y-%m-%d %H:%M:%S]')
        if log:
            dir_path = os.path.split(path)[0]
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
            if not os.path.exists(path):
                os.mknod(path)
            handler = logging.FileHandler(path)
            handler.setLevel(logging.INFO)
            handler.setFormatter(formatter)
            self.addHandler(handler)
        if console:
            console = logging.StreamHandler()
            console.setLevel(level)
            console.setFormatter(formatter)
            self.addHandler(console)
