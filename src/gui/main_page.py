"""
GUI
"""
from nicegui import ui

from . import settings_drawer, logging_footer, gui_events
from .gui_style import page_title_style

@ui.page('/')
def draw_page():
    with ui.header().classes('place-content-center') as header:
        #ui.button(on_click=lambda: left_drawer.toggle(), icon='settings').props('flat color=white')
        ui.label('SmartOxigen').style(page_title_style).classes('mx-auto italic')
        """
        with ui.tabs() as tabs:
            config = ui.tab('Race configuration', icon='edit_road').style('font-size: 130%')
            data = ui.tab('Race data', icon='sports_motorsports').style('font-size: 130%')
            #print(dir(data.props))
            data.color = 'secondary#
        """


    with ui.left_drawer().classes('bg-blue-100') as left_drawer:
        settings_drawer.draw()

    with ui.footer(value=False).classes('bg-orange-100') as footer:
        logging_footer.draw()
    """
    with ui.tab_panels(tabs, value=config).classes('w-full'):
        pass
    """

    with ui.page_sticky(position='bottom-left', x_offset=20, y_offset=20):
        ui.button(on_click=left_drawer.toggle, icon='settings').props('fab')

    with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
        ui.button(on_click=footer.toggle, icon='assignment', color='bg-orange-100').props('fab')

    gui_events.push_notify_request.subscribe(lambda msg,typ: ui.notify(msg,type=typ))