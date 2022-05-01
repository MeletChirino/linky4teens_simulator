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
                print("RACE")
                return 0
            elif event == SERIAL_EXIST:
                self.state = 2
                print("0 -> 2")
                print("DATA_TRANSFER")
                return 0
        # --- state 1 transitions ---
        if self.state == 1:
            if event == END_RACE:
                self.state = 0
                print("1 -> 0")
                print("STD_BY")
                return 0
            if event == RELAY_ZONE_ENTRY_EVENT:
                self.state = 3
                print("1 -> 3")
                print("RELAY ZONE")
                return 0
        # --- state 2 transitions ---
        if self.state == 2 and event == END_SERIAL:
            self.state = 0
            print("2 -> 0")
            print("STD_BY")
            return 0
        # --- state 3 transitions ---
        if self.state == 3:
            if event == RELAY_EVENT:
                self.state = 4
                print("3 -> 4")
                print("GOOD RELAY")
                return 0
            if event == RELAY_ZONE_EXIT_EVENT:
                self.state = 1
                print("3 -> 1")
                print("BAD RELAY")
                print("RACE")
                return 0
        # --- state 4 transitions ---
        if self.state == 4 and event == RELAY_ZONE_EXIT_EVENT:
            self.state = 1
            print("4 -> 1")
            print("RACE")
            return 0

    def state_function(self):
        if self.state == 0:
            pass
        elif self.state == 5:
            pass
        elif self.state == 2:
            pass

