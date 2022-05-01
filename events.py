from components.atomic_state_machine import Event

START_RACE = Event('start_race')
END_RACE = Event('end_race')
SERIAL_EXIST = Event('serial_exist')
END_SERIAL = Event('end_serial')
RELAY_ZONE_ENTRY_EVENT =  Event('relay_zone_entry')
RELAY_ZONE_EXIT_EVENT = Event('relay_zone_exit')
RELAY_EVENT = Event('relay')
