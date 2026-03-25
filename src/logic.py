import asyncio

import shared_data
#import shared_data
from nicegui import ui
from gui import gui_events
from smartrace.smartrace_main import smartrace_connect
from smartrace.smartrace_events import smartrace_events


##############################
# Connection handling events
##############################
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

##############################
# player handling events
##############################
@smartrace_events.player_list.connect
def smartrace_player_list(data: dict):
    print('Received smartrace player list')
    print(data)
    #for key,player in data.items():
    #    gui_events.smartrace_player_update_request.emit(key, player['backgroundColor'], player['driver'], player['car'])
    shared_data.player_1_driver = data['1']['driver']
    shared_data.player_1_car = data['1']['car']
    shared_data.player_1_color = data['1']['color']
    shared_data.player_1_bgcolor = data['1']['backgroundColor']
    shared_data.player_2_driver = data['2']['driver']
    shared_data.player_2_car = data['2']['car']
    shared_data.player_2_color = data['2']['color']
    shared_data.player_2_bgcolor = data['2']['backgroundColor']
    shared_data.player_3_driver = data['3']['driver']
    shared_data.player_3_car = data['3']['car']
    shared_data.player_3_color = data['3']['color']
    shared_data.player_3_bgcolor = data['3']['backgroundColor']
    shared_data.player_4_driver = data['4']['driver']
    shared_data.player_4_car = data['4']['car']
    shared_data.player_4_color = data['4']['color']
    shared_data.player_4_bgcolor = data['4']['backgroundColor']
    shared_data.player_5_driver = data['5']['driver']
    shared_data.player_5_car = data['5']['car']
    shared_data.player_5_color = data['5']['color']
    shared_data.player_5_bgcolor = data['5']['backgroundColor']
    shared_data.player_6_driver = data['6']['driver']
    shared_data.player_6_car = data['6']['car']
    shared_data.player_6_color = data['6']['color']
    shared_data.player_6_bgcolor = data['6']['backgroundColor']
    gui_events.smartrace_player_color_update_request.emit()
