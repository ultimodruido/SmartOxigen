from nicegui import app
import shared_data

shared_data.smartrace_server = app.storage.general.get('smartrace_server', '')
shared_data.smartrace_port = app.storage.general.get('smartrace_port', 8080)
shared_data.smartrace_fuel_addon = app.storage.general.get('smartrace_fuel_addon', False)
shared_data.smartrace_penalty_addon = app.storage.general.get('smartrace_penalty_addon', False)

shared_data.oxigen_dongle_port = app.storage.general.get('oxigen_dongle_port', 'COM2')
shared_data.oxigen_max_speed = app.storage.general.get('oxigen_max_speed', 255)
shared_data.oxigen_pitlane_trigger = app.storage.general.get('oxigen_pitlane_trigger', False)
shared_data.oxigen_pitlane_entry = app.storage.general.get('oxigen_pitlane_entry', 'Pit leave')

def save_smartrace_settings():
    app.storage.general['smartrace_server'] = shared_data.smartrace_server
    app.storage.general['smartrace_port'] = shared_data.smartrace_port
    #app.storage.general['smartrace_director_view'] = shared_data.smartrace_director_view
    app.storage.general['smartrace_fuel_addon'] = shared_data.smartrace_fuel_addon
    app.storage.general['smartrace_penalty_addon'] =shared_data.smartrace_penalty_addon

def save_oxigen_settings():
    app.storage.general['oxigen_dongle_port'] = shared_data.oxigen_dongle_port
    app.storage.general['oxigen_max_speed'] = shared_data.oxigen_max_speed
    app.storage.general['oxigen_pitlane_trigger'] = shared_data.oxigen_pitlane_trigger
    app.storage.general['oxigen_pitlane_entry'] = shared_data.oxigen_pitlane_entry