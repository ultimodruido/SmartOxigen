# SmartOxigen

Bridge between Slot.it Oxigen hardware and Smartrace race management app. Early-stage project.

## Stack

- Python 3.12+, uv for package management
- NiceGUI (web UI framework)
- psygnal (signal/slot event system)
- websockets (Smartrace connection)
- pyserial (Oxigen dongle connection)

## Run

```bash
cd src && python main.py
```

## Project Structure

```
src/
  main.py          # NiceGUI entry point (ui.run())
  logic.py         # Central hub connecting GUI, Smartrace, Oxigen blocks
  shared_data.py   # Module-level state shared across components
  store_settings.py # NiceGUI persistent settings storage
  gui/             # NiceGUI UI components
  smartrace/       # WebSocket client for Smartrace API
  oxigen/          # Oxigen dongle interface
submodules/oxigenlib/  # Git submodule - run `git submodule update --init`
```

## Architecture

Three macro-blocks connect the system:
1. **GUI** - NiceGUI UI components with its own event system
2. **Smartrace** - websocket client (`smartrace_main.py`) using psygnal signals
3. **Oxigen** - serial dongle interface (`oxigen_main.py`) using psygnal signals

Smartrace and Oxigen blocks communicate via psygnal signal/slot events.
GUI events use NiceGUI's built-in event system.

`logic.py` subscribes to all events and bridges between the three blocks.

`shared_data.py` - Module-level state shared across components (player data, race status, settings)

`store_settings.py` - NiceGUI persistent settings storage (app.storage.general)

## Git Submodule

The `oxigenlib` dependency is a git submodule. After cloning:
```bash
git submodule update --init
```
