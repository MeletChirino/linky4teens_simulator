'''This file links cyclic event with tasks'''
# python modules
from time import time as current_time

# local module
from components.time_based_event import TimeBasedEvent
from components.irq_event import IRQEvent
from events import *
from components.temoin import TEMOIN_HL

VIBRATE_TASK = TimeBasedEvent(
        TEMOIN_HL.vibrate,
        10
        )

BLINK_RED_TASK = TimeBasedEvent(
        TEMOIN_HL.led.blink_red,
        100
        )
BLINK_GREEN_TASK = TimeBasedEvent(
        TEMOIN_HL.led.blink_green,
        100
        )
