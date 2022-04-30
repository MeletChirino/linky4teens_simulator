class Event:
    def __init__(self, name):
        self.name = name
        self.sm_list = []

    def attach(self, SM):
        self.sm_list.append(SM)

    def dettach(self, SM):
        self.sm_list.pop(SM)

    def happen(self, value):
        for sm in self.sm_list:
            sm.transition(self)
            sm.state_function()

class AtomicStateMachine:
    def __init__(self, name, **kwargs):
        self.state = 0
        self.name = name
        self.transition_list = []
        # actual_state, event, next_state
        self.state_names = []
        if kwargs.get('state_names'):
            self.state_names = kwargs['state_names']

    def state_names(self, *state_names):
        self.state_names = state_names

    def reset(self):
        self.state = 0

    def transition(self, event):
        pass

    def state_function(self):
        pass

    def attach_events(self, *events):
        for event in events:
            event.attach(self)
