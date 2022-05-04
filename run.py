# python modules import pygame

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
    op_machine.set_transition_list(
            # (init_state, next_state, [function_list], event)
            # STD By state (0)
            (0, 1, [BLINK_YELLOW_TASK.disable, BLINK_RED_TASK.disable, BLINK_GREEN_TASK.disable, TEMOIN_HL.led.set_blue], START_RACE_EVENT),
            (0, 4, [], CONNECT_EVENT),
            # Race state (1)
            (1, 2, [VIBRATE_TASK.enable, TEMOIN_HL.led.reset_blink], RELAY_ZONE_ENTRY_EVENT),
            (1, 0, [TEMOIN_HL.led.set_yellow], END_RACE_EVENT),
            # Relay zone (2)
            (2, 1, [BLINK_RED_TASK.enable, VIBRATE_TASK.disable], RELAY_ZONE_EXIT_EVENT),
            (2, 3, [BLINK_GREEN_TASK.enable, VIBRATE_TASK.disable], RELAY_EVENT),
            # Good Relay (3)
            (3, 1, [TEMOIN_HL.led.set_blue], RELAY_ZONE_EXIT_EVENT),
            # Connected Pc (4)
            (4, 4, [BLINK_YELLOW_TASK.enable, send_data], DATA_REQUEST_EVENT),
            (4, 0, [TEMOIN_HL.led.set_yellow, SEND_DATA_TASK.disable], DISCONNECT_EVENT),
            )
    op_machine.set_state_function_list(
            [],
            [BLINK_RED_TASK.update],
            [VIBRATE_TASK.update],
            [BLINK_GREEN_TASK.update],
            [BLINK_YELLOW_TASK.update],#send data 
            )

    # --- event attaching ---
    op_machine.attach_events(
            # race related events
            START_RACE_EVENT,
            END_RACE_EVENT,
            # relay related events
            RELAY_EVENT,
            RELAY_ZONE_ENTRY_EVENT,
            RELAY_ZONE_EXIT_EVENT,
            # connectivity relate events
            CONNECT_EVENT,
            DISCONNECT_EVENT,
            DATA_REQUEST_EVENT,
            )

    while(game.running):
        game.gameloop()
        op_machine.state_function()
        for delimiter in game.delimiters:
            if delimiter.cross(game.athlete.x):
                if delimiter.type == START_RACE_DELIMITER:
                    START_RACE_EVENT.happen(1)
                if delimiter.type == END_RACE_DELIMITER:
                    END_RACE_EVENT.happen(1)
                if delimiter.type == START_ZONE_DELIMITER:
                    RELAY_ZONE_ENTRY_EVENT.happen(1)
                if delimiter.type == END_ZONE_DELIMITER:
                    RELAY_ZONE_EXIT_EVENT.happen(1)

if __name__ == "__main__":
    main()
