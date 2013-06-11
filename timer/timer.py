import time


class Timer(object):
    def __init__(self):
        self.tstart = None

    @property
    def elapsed(self):
        return time.time() - self.tstart

    def __enter__(self):
        self.tstart = time.time()
        self.on_enter()
        return self

    def on_enter(self):
        pass

    def __exit__(self, type=None, value=None, traceback=None):
        self.on_exit()

    def on_exit(self):
        pass

    def start(self):
        self.__enter__()

    def stop(self):
        self.__exit__()


class LogTimer(Timer):
    """ Adds a log output when the timer exits """
    def __init__(self, logfunc, logmessage=None):
        super(LogTimer, self).__init__()

        self.log = logfunc
        if not self.log:
            import logging
            logging.basicConfig()
            self.log = logging.info()

        self.message = logmessage
        if not self.message:
            self.message = 'Elapsed time: {:.4f} seconds'

    def on_exit(self):
        message = self.message.format(self.elapsed)
        self.log(message)


def log_demo():

    # LogTimer demo
    import logging
    logging.basicConfig()
    log = logging.getLogger('test')
    log.setLevel(logging.DEBUG)
    retval = 0
    with LogTimer(logfunc=log.info):
        for i in range(1000001):
            retval += i
    log.info(retval)

def basic_demo():
    # basic timer demo
    retval = 0
    with Timer() as a:
        for i in range(10000):
            retval += 1
        print a.elapsed

def start_stop_demo():
    # start / stop demo
    def fib(x):
        p0 = 0
        p1 = 1

        yield p1

        for i in xrange(x):
            yield p0 + p1
            new = p0 + p1
            p0 = p1
            p1 = new

    t = Timer()
    t.start()

    print list(fib(10))

    t.stop()
    print t.elapsed

if __name__ == '__main__':
    basic_demo()
    start_stop_demo()
    log_demo()
