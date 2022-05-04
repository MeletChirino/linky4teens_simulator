class Event:
    def __init__(self, name):
        self.name = name
        self.sm_list = []

    def attach(self, SM):
        self.sm_list.append(SM)

    def dettach(self, SM):
        self.sm_list.pop(SM)

    def happen(self, value):
        print(F"HAPPEN \n---- {self.name} ----")
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
        self.transition_list = []
        self.state_function_list = []
        if kwargs.get('state_names'):
            self.state_names = kwargs['state_names']

    def state_names(self, *state_names):
        self.state_names = state_names

    def set_transition_list(self, *transition_list):
        # transition format (init_state, next_state, [function], event)
        for transition in transition_list:
            if len(transition) != 4:
                raise Exception("Unvalid Transition Format")
            else:
                self.transition_list.append(transition)

    def reset(self):
        self.state = 0

    def transition(self, event):
        for transition in self.transition_list:
            if self.state == transition[0]:
                if event == transition[3]:
                    print(F"{transition[0]} -> {transition[1]} : {transition[3].name}")
                    self.state = transition[1]
                    if len(transition[2]) > 0:
                        print(transition[2])
                        for func in transition[2]:
                            func()
                        return 0

    def attach_events(self, *events):
        for event in events:
            event.attach(self)

    def set_state_function_list(self, *state_function_list):
        # Functions should be written in same state order, it MUST be a list of functions, if no functions place empty list
        for state_function in state_function_list:
            self.state_function_list.append(state_function)

    def state_function(self):
        funcs = self.state_function_list[self.state]
        if len(funcs) > 0:
            for func in funcs:
                func()
