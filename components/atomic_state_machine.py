class AtomicStateMachine:
    def __init__(self, name):
        self.state = 0

    def state_names(self, *state_names):
        self.state_names = *state_names

    def reset(self):
        self.state = 0

    def transmission(self, event):
        pass

    def state_function(self):
        pass
