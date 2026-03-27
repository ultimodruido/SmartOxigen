import shared_data
from nicegui import ui
from contextlib import contextmanager

from .gui_style import page_card_title_style
from . import gui_events


@contextmanager
def content() -> None:
    ui.colors(racebg='#4cb28d', racetxt='white')
    with ui.card():
        btn_race = {
            'running': False,
            'suspended': False,
            'starting': False,
            'ended': True,
        }

        ui.label('Race Status').style(page_card_title_style).classes('mx-auto')
        ui.separator()
        ui.button('GREEN FLAG', color='positive').classes('w-full py-8').bind_visibility_from(btn_race, 'running')
        ui.button('RED FLAG', color='negative').classes('w-full py-8').bind_visibility_from(btn_race, 'suspended')
        ui.button('STARTING', color='warning').classes('w-full py-8').bind_visibility_from(btn_race, 'starting')
        ui.button('ENDED', color='dark').classes('w-full py-8').bind_visibility_from(btn_race, 'ended')


        @gui_events.smartrace_race_update_status.subscribe
        def race_status_update(status: str) -> None:
            if status not in btn_race.keys():
                status = 'ended'
            for key in btn_race.keys():
                btn_race[key] = False
            btn_race[status] = True