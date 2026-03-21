"""
Webserver application to bridge the gap between slot race track controlled
by the **slot.it oxigen** system and the **smartrace RMS app**.
"""
from nicegui import ui
import logic

# TODO import settings
# usare nicegui
import store_settings

# create the ui page
import gui.main_page


ui.run()