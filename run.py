# python modules
import pygame

# local modules
from components.time_based_event import TimeBasedEvent
from components.operative_sm import OperativeSM
from components.atomic_state_machine import Event
from events import *
from tasks import *
from kernel.sim_elements import (
        START_ZONE_DELIMITER, END_ZONE_DELIMITER,
        START_RACE_DELIMITER, END_RACE_DELIMITER
        )
from kernel.sim import RaceGame


def main():
    game = RaceGame(
            screen_size = [1300, 200],
            )
    op_machine = OperativeSM('OpMachine')
    # --- event attaching ---
    op_machine.attach_events(
            # race related events
            START_RACE_EVENT,
            END_RACE_EVENT,
            # relay related events
            RELAY_EVENT,
            RELAY_ZONE_ENTRY_EVENT,
            RELAY_ZONE_EXIT_EVENT
            # connectivity relate events
            CONNECT_EVENT,
            DISCONNECT_EVENT,
            DATA_REQUEST_EVENT,
            )

    while(game.running):
        game.gameloop()
        VIBRATE_TASK.update()
        BLINK_RED_TASK.update()
        BLINK_GREEN_TASK.update()
        for delimiter in game.delimiters:
            if delimiter.cross(game.athlete.x):
                if delimiter.type == START_RACE_DELIMITER:
                    START_RACE.happen(1)
                if delimiter.type == END_RACE_DELIMITER:
                    END_RACE.happen(1)
                if delimiter.type == START_ZONE_DELIMITER:
                    RELAY_ZONE_ENTRY_EVENT.happen(1)
                if delimiter.type == END_ZONE_DELIMITER:
                    RELAY_ZONE_EXIT_EVENT.happen(1)


if __name__ == "__main__":
    main()
