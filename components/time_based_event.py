import time

class TimeBasedEvent:
    def __init__(self, func, period, **kwargs):
        self.func = func
        self.period = period
        self.enabled = False
        self.last_time = time.time()
        if kwargs.get('enabled'):
            self.enabled = kwargs['enabled']

    def enable(self):
        self.enabled = True
        self.last_time = time.time()

    def disable(self):
        self.enabled = False
        self.last_time = time.time()

    def update(self):
        current_time = time.time()
        passed_time = current_time - self.last_time
        if (passed_time >= self.period and self.enabled):
            self.last_time = current_time
            self.func()
