"""
GUI
"""
from nicegui import ui

from . import settings_drawer, logging_footer, gui_events
from .gui_style import page_title_style
from . import card_players, card_race_status

@ui.page('/')
def draw_page():

    with ui.left_drawer().classes('bg-blue-100') as left_drawer:
        settings_drawer.draw()

    with ui.header().classes('place-content-center') as header:
        ui.button(on_click=left_drawer.toggle, icon='settings').props('fab color=warning')
        ui.label('SmartOxigen').style(page_title_style).classes('mx-auto italic')

    # TODO main page content will be a list of cards
    # to be included in order of appearance
    # make a list to be able to sort elements in and out
    with ui.grid(columns=4).classes('w-full'):
        card_race_status.content()
        card_players.content()

    with ui.footer(value=False).classes('bg-orange-100') as footer:
        logging_footer.draw()

    with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
        ui.button(on_click=footer.toggle, icon='assignment', color='bg-orange-100').props('fab')

    gui_events.push_notify_request.subscribe(lambda msg,typ: ui.notify(msg,type=typ))