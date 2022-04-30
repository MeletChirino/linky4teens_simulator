# local modules
from components.time_based_event import TimeBasedEvent
from components.operative_sm import OperativeSM
from components.atomic_state_machine import Event
from events import *
from tasks import *


def main():
    op_machine = OperativeSM('OpMachine')
    # --- event attaching ---
    op_machine.attach_events(
            START_RACE,
            END_RACE,
            SERIAL_EXIST,
            END_SERIAL
            )

    while(True):
        START_RACE_TASK.update()
        END_RACE_TASK.update()
        SERIAL_EXIST_TASK.update()
        END_SERIAL_TASK.update()


if __name__ == "__main__":
    main()
