import time

class IRQEvent:
    def __init__(self, func, period, **kwargs):
        self.func = func
        self.period = period
        self.enabled = False
        self.last_time = time.time() * 1000
        if kwargs.get('enabled'):
            self.enabled = kwargs['enabled']
        if kwargs.get('start_time'):
            self.last_time -= (self.period + kwargs['start_time'])

    def enable(self):
        self.enabled = True
        self.last_time = time.time()

    def disable(self):
        self.enabled = False
        self.last_time = time.time()

    def update(self):
        current_time = time.time() * 1000
        passed_time = current_time - self.last_time
        if (passed_time >= self.period and self.enabled):
            self.func()
            self.disable()
