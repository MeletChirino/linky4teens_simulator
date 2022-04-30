# python modules
from time import time as current_time

# local module
from components.time_based_event import TimeBasedEvent
from components.irq_event import IRQEvent
from events import *

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

START_RACE_TASK = IRQEvent(
        task300ms,
        300,
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
