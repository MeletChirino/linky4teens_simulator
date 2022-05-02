from components.atomic_state_machine import Event

START_RACE_EVENT = Event('start_race')
END_RACE_EVENT = Event('end_race')
RELAY_ZONE_ENTRY_EVENT =  Event('relay_zone_entry')
RELAY_ZONE_EXIT_EVENT = Event('relay_zone_exit')
RELAY_EVENT = Event('relay')
DATA_REQUEST_EVENT = Event('data_request')
CONNECT_EVENT = Event('connect')
DISCONNECT_EVENT = Event('disconnect')
