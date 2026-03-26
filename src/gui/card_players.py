import shared_data
from nicegui import ui
from contextlib import contextmanager

from .gui_style import page_card_title_style
from . import gui_events


@contextmanager
def content() -> None:
    ui.colors(
        one='#4cb28d', onet='white',
        two='#4cb28d', twot='white',
        three='#4cb28d', threet='white',
        four='#4cb28d', fourt='white',
        five='#4cb28d', fivet='white',
        six='#4cb28d', sixt='white'
    )
    with ui.card().classes('row-span-3'):
        ui.label('Players list').style(page_card_title_style).classes('mx-auto')
        ui.separator()
        with ui.list(): #.props('bordered separator')
            with ui.item():
                with ui.item_section().props('avatar'):
                    with ui.element('div').classes('px-4 py-2 rounded-md bg-one'):
                        ui.label('1').classes('text-onet')
                with ui.item_section():
                    ui.item_label('Player').bind_text_from(shared_data,'player_1_driver')
                    ui.item_label('BMW M4').props('caption').bind_text_from(shared_data,'player_1_car')
                with ui.item_section().props('side'):
                    ui.icon('tablet_android').bind_visibility_from(shared_data,'player_1_smartrace_active')
                with ui.item_section().props('side'):
                    ui.icon('directions_car').bind_visibility_from(shared_data,'player_1_oxigen_active')
            ui.separator()
            with ui.item():
                with ui.item_section().props('avatar'):
                    with ui.element('div').classes('px-4 py-2 rounded-md bg-two'):
                        ui.label('2').classes('text-twot')
                with ui.item_section():
                    ui.item_label('Player').bind_text_from(shared_data,'player_2_driver')
                    ui.item_label('BMW M4').props('caption').bind_text_from(shared_data,'player_2_car')
                with ui.item_section().props('side'):
                    ui.icon('tablet_android').bind_visibility_from(shared_data,'player_2_smartrace_active')
                with ui.item_section().props('side'):
                    ui.icon('directions_car').bind_visibility_from(shared_data,'player_2_oxigen_active')
            ui.separator()
            with ui.item():
                with ui.item_section().props('avatar'):
                    with ui.element('div').classes('px-4 py-2 rounded-md bg-three'):
                        ui.label('3').classes('text-threet')
                with ui.item_section():
                    ui.item_label('Player').bind_text_from(shared_data,'player_3_driver')
                    ui.item_label('BMW M4').props('caption').bind_text_from(shared_data,'player_3_car')
                with ui.item_section().props('side'):
                    ui.icon('tablet_android').bind_visibility_from(shared_data,'player_3_smartrace_active')
                with ui.item_section().props('side'):
                    ui.icon('directions_car').bind_visibility_from(shared_data,'player_3_oxigen_active')
            ui.separator()
            with ui.item():
                with ui.item_section().props('avatar'):
                    with ui.element('div').classes('px-4 py-2 rounded-md bg-four'):
                        ui.label('4').classes('text-fourt')
                with ui.item_section():
                    ui.item_label('Player').bind_text_from(shared_data,'player_4_driver')
                    ui.item_label('BMW M4').props('caption').bind_text_from(shared_data,'player_4_car')
                with ui.item_section().props('side'):
                    ui.icon('tablet_android').bind_visibility_from(shared_data,'player_4_smartrace_active')
                with ui.item_section().props('side'):
                    ui.icon('directions_car').bind_visibility_from(shared_data,'player_4_oxigen_active')
            ui.separator()
            with ui.item():
                with ui.item_section().props('avatar'):
                    with ui.element('div').classes('px-4 py-2 rounded-md bg-five'):
                        ui.label('5').classes('text-fivet')
                with ui.item_section():
                    ui.item_label('Player').bind_text_from(shared_data,'player_5_driver')
                    ui.item_label('BMW M4').props('caption').bind_text_from(shared_data,'player_5_car')
                with ui.item_section().props('side'):
                    ui.icon('tablet_android').bind_visibility_from(shared_data,'player_5_smartrace_active')
                with ui.item_section().props('side'):
                    ui.icon('directions_car').bind_visibility_from(shared_data,'player_5_oxigen_active')
            ui.separator()
            with ui.item():
                with ui.item_section().props('avatar'):
                    with ui.element('div').classes('px-4 py-2 rounded-md bg-six'):
                        ui.label('6').classes('text-sixt')
                with ui.item_section():
                    ui.item_label('Player').bind_text_from(shared_data,'player_6_driver')
                    ui.item_label('BMW M4').props('caption').bind_text_from(shared_data,'player_6_car')
                with ui.item_section().props('side'):
                    ui.icon('tablet_android').bind_visibility_from(shared_data,'player_6_smartrace_active')
                with ui.item_section().props('side'):
                    ui.icon('directions_car').bind_visibility_from(shared_data,'player_6_oxigen_active')

        @gui_events.smartrace_player_color_update_request.subscribe
        def player_color_update():
            #print('Color update event')

            def hex_color(s):
                if s[0] == '#':
                    return s
                if s[0:3] == 'rgb':
                    r, g, b = s[4:-1].split(',')
                    h = '#%02x%02x%02x' % (int(r.strip()), int(g.strip()), int(b.strip()))
                    #print(r, g, b, h)
                    return h
                return s
            ui.colors(
                onet=hex_color(shared_data.player_1_color),
                twot=hex_color(shared_data.player_2_color),
                threet=hex_color(shared_data.player_3_color),
                fourt=hex_color(shared_data.player_4_color),
                fivet=hex_color(shared_data.player_5_color),
                sixt=hex_color(shared_data.player_6_color),
                one=hex_color(shared_data.player_1_bgcolor),
                two=hex_color(shared_data.player_2_bgcolor),
                three=hex_color(shared_data.player_3_bgcolor),
                four=hex_color(shared_data.player_4_bgcolor),
                five=hex_color(shared_data.player_5_bgcolor),
                six=hex_color(shared_data.player_6_bgcolor),
            )