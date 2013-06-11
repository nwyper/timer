from timer import Timer

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
