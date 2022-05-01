'''This file links cyclic event with tasks'''
# python modules
from time import time as current_time

# local module
from components.time_based_event import TimeBasedEvent
from components.irq_event import IRQEvent
from events import *
from components.temoin import TEMOIN_HL

def task300ms():
    START_RACE.happen(2)
    print("300ms task:", current_time(), "\n -----\n")

def task500ms():
    END_RACE.happen(2)
    print("500ms task:", current_time(), "\n -----\n")

def task800ms():
    SERIAL_EXIST.happen(1)
    print("800ms task:", current_time(), "\n -----\n")

def task4000ms():
    END_SERIAL.happen(1)
    print("4000ms task:", current_time(), "\n -----\n")

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
START_RACE_TASK = IRQEvent(
        task300ms,
        30,
        enabled = True
        )

END_RACE_TASK = IRQEvent(
        task500ms,
        500,
        enabled = True
        )
SERIAL_EXIST_TASK = TimeBasedEvent(
        task800ms,
        800,
        enabled = True
        )

END_SERIAL_TASK = TimeBasedEvent(
        task4000ms,
        4000,
        enabled = True
        )
