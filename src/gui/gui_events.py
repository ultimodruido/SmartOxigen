from nicegui import Event

push_notify_request = Event[str,str]()
smartrace_connect_request = Event[str, int]()
smartrace_player_color_update_request = Event()
