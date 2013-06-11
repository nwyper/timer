#!/usr/bin/python

from timer import Timer, LogTimer


def basic_demo():
    # basic timer demo
    print "\nBasic timer demo, using 'with' statement"
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

    print "\nBasic timer demo, using 'start/stop'"

    t = Timer()
    t.start()

    x = list(fib(1000))

    t.stop()
    print t.elapsed


def log_demo():
    # LogTimer demo
    print "\nLogTimer demo"

    # set up logger
    import logging
    logging.basicConfig()
    log = logging.getLogger('test')
    log.setLevel(logging.DEBUG)

    # run test
    retval = 0
    with LogTimer(logfunc=log.info):
        for i in range(1000001):
            retval += i
        # timing result is automatically logged, with level 'INFO'

    # log result
    log.info(retval)


if __name__ == '__main__':
    basic_demo()
    start_stop_demo()
    log_demo()
