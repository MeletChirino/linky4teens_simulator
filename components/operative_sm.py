# python modules
from time import time as current_time

# local modules
from components.atomic_state_machine import AtomicStateMachine
from events import *
from tasks import *
from components.temoin import TEMOIN_HL

class OperativeSM(AtomicStateMachine):
    def __init__(self, name, **kwargs):
        super().__init__(name)
