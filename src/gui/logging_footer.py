from nicegui import ui
from .gui_style import log_style


def draw():
    ui.label('Logger').style(log_style)
    log = ui.log(max_lines=20).classes('w-full h-60')

