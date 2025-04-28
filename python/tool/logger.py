import logging

# ttest
class Logger(logging.getLoggerClass()):

    def __init__(self, name, log=False, console=True, level=logging.INFO, path='log.log'):
        super().__init__(name, level)
        formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s %(filename)s %(funcName)s line%(lineno)d:%(message)s',
                                      datefmt='[%Y-%m-%d %H:%M:%S]')
        if log:
            handler = logging.FileHandler(path)
            handler.setLevel(logging.INFO)
            handler.setFormatter(formatter)
            self.addHandler(handler)
        if console:
            console = logging.StreamHandler()
            console.setLevel(level)
            console.setFormatter(formatter)
            self.addHandler(console)
