# python modules
from time import time as current_time

# local modules
from components.atomic_state_machine import AtomicStateMachine
from events import *
from tasks import *

class OperativeSM(AtomicStateMachine):
    def __init__(self, name, **kwargs):
        super().__init__(name)

    def transition(self, event):
        # --- state 0 transitions ---
        if self.state == 0:
            if event == START_RACE:
                self.state = 1
                print("0 -> 1")
            elif event == SERIAL_EXIST:
                self.state = 2
                print("0 -> 2")
        # --- state 1 transitions ---
        if self.state == 1 and event == END_RACE:
            self.state = 0
            print("1 -> 0")
        # --- state 2 transitions ---
        if self.state == 2 and event == END_SERIAL:
            self.state = 0
            print("2 -> 0")

    def state_function(self):
        if self.state == 0:
            print("STD_BY")
            SERIAL_EXIST_TASK.enable()
        elif self.state == 1:
            print("RACE")
            START_RACE_TASK.disable()
        elif self.state == 2:
            print("DATA_TRANSFER")
            SERIAL_EXIST_TASK.disable()

