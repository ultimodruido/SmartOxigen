from psygnal import Signal

class Events:
# emit smartrace_connection_succesfull
# emit smartrace_connection_closed

    # notify a successful connection
    connection_successful = Signal()

    # notify an interrupted connection
    connection_closed = Signal()

    # notify received API version
    api_version = Signal(int)

    """
    # info new data available ready for transmission
    transmit_command_event = Signal(bytes)
    # new data arrived from the dongle
    dongle_new_data_available_event = Signal(DongleRxData)
    # dongle wrong cache length - need flush
    dongle_flush_cache = Signal()

    # module events
    # new lap event : id / timestamp / laptime / info_flag
    new_lap_event = Signal(int, int, int, float, bool)
    # pit enter-leave : event id / timestamp
    pit_lane_enter_event = Signal(int, int)
    pit_lane_leave_event = Signal(int, int)
    # global event
    track_call_event = Signal(bool, list)
    all_cars_on_track_event = Signal(bool, list)
    """

smartrace_events = Events()