from random import randint # TODO remove when updated

from nicegui import ui, run
from .gui_style import text_style_big, text_style
from .gui_events import smartrace_connect_request
#from smartrace.smartrace_main import smartrace_connect

import shared_data
import store_settings
"""
import importlib.util
path = "../"
mname = "shared_data"

# Load module from specified file location
spec = importlib.util.spec_from_file_location(mname, path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
"""

def draw() -> None:

    ui.label('Settings').style(text_style_big).classes('mx-auto')
    with ui.card().classes('w-60 mx-auto') as smartrace_cgf:
        ui.image('./assets/smartrace.png').classes('w-30 mx-auto')
        ui.separator()
        #ui.label('Smartrace server:').style(text_style)
        with ui.row(): #.classes('grow justify-items-center'):
        #sr_server = ui.label('---.---.---.---:xxxx').style(text_style)
            sr_dialog_server = ui.input('Server IP:', placeholder='localhost').classes('w-25').bind_value(shared_data,'smartrace_server')
            sr_dialog_port = ui.input('Port:', placeholder='8080').classes('w-15').bind_value(shared_data,'smartrace_port')
            #ui.button(icon='edit_note', on_click=sr_dialog.open)
        sr_fuel = ui.switch('Add-On fuel simulation available?').style(text_style).bind_value(shared_data,'smartrace_fuel_addon')
        sr_penalty = ui.switch('Add-On penalty available?').style(text_style).bind_value(shared_data,
                                                                                              'smartrace_penalty_addon')

        ui.separator()
        ui.button('Connect', icon='wifi', on_click=lambda: sr_connect()).classes('mx-auto px-6 py-2')

        async def sr_connect():
            print('Connecting to Smartrace')
            #await run.io_bound(smartrace_connect, shared_data.smartrace_server, shared_data.smartrace_port)
            smartrace_connect_request.emit(shared_data.smartrace_server, shared_data.smartrace_port)
            store_settings.save_smartrace_settings()
            #await smartrace_connect(shared_data.smartrace_server, shared_data.smartrace_port)
            #print('Connected to Smartrace')
            #ui.notify('Smartrace connection lost..', type='negative')

            #else:
            #    ui.notify('Impossible to connect to Smartrace...', type='warning')

    with ui.card().classes('w-60 mx-auto') as oxigen_cgf:
        ui.image('./assets/oxigen.jpg').classes('w-30 mx-auto')
        ui.separator()
        with ui.row().classes('grow justify-items-center'):
            def check_v(val):
                try:
                    val = int(val)
                    if val < 0 or val > 255:
                        return "Insert a number between 0 and 255"
                    return None
                except Exception as e:
                    return "Insert a number between 0 and 255"
            ui.input('Dongle port', placeholder='example: COM2').classes('w-22').bind_value(shared_data,'oxigen_dongle_port')
            ui.number('Max speed',
                      value=255,
                      min=0, max=255,
                      precision=0,
                      validation=lambda v: check_v(v)).classes('w-22').bind_value(shared_data,'oxigen_max_speed') #, validation=lambda v: check_v(v)

        #ui.separator()
        pit_lap_count = ui.switch('Pitlane trigger lap count?').style(text_style).bind_value(shared_data,'oxigen_pitlane_trigger')
        pit_lap_cfg = ui.radio(['Pit entry', 'Pit leave'], value='Pit leave'    ).style(text_style).bind_value(shared_data,'oxigen_pitlane_entry')
        pit_lap_count.bind_value_to(pit_lap_cfg, 'visible')

        ui.separator()
        ui.button('Connect', icon='cable', on_click=lambda: ox_connect()).classes('mx-auto px-6 py-2')

        def ox_connect():
            #print('Connected to Smart Oxigen server')
            store_settings.save_oxigen_settings()
            ui.notify('Oxigen connection successful..', type='positive')

