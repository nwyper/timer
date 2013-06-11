#!/usr/bin/python

from timer import Timer, LogTimer


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
