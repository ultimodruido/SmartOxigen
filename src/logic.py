import asyncio
#import shared_data
from nicegui import ui
from gui import gui_events
from smartrace.smartrace_main import smartrace_connect
from smartrace.smartrace_events import smartrace_events


@gui_events.smartrace_connect_request.subscribe
async def smartrace_connect_request(server: str, port: int):
    print(f'Connectiong "{server}"...{port}')
    await smartrace_connect(server, str(port))
    #await asyncio.sleep(1)  # simulate writing to database

@smartrace_events.connection_successful.connect
def smartrace_connection_successful():
    print('Connection successful')
    gui_events.push_notify_request.emit('Smartrace connection successful','positive')
    #ui.notify('Connected to Smartrace...', type='positive')

@smartrace_events.connection_closed.connect
def smartrace_connection_closed():
    print('Connection closed')
    gui_events.push_notify_request.emit('Smartrace connection broken', 'warning')
    #ui.notify('Connection to Smartrace broke...', type='warning')
