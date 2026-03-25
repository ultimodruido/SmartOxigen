"""
Smartrace API
this file is the entry point to manage the websocket connection with smartrace
It contains:

async main loop
manage 2 sockets
signal/slot infrastructure
state machine:
- not connected
- connected
  - catch LostConnection exception
  - read messages in async and emit corresponding signal
"""
import asyncio
import json

from websockets.asyncio.client import connect, ClientConnection
from websockets.exceptions import ConnectionClosed

from .smartrace_events import smartrace_events

_messages_queue = list()

async def smartrace_send(connection:ClientConnection):
    pass

managed_events = {
    "update_controller_data": smartrace_events.player_list,
    "api_version": smartrace_events.api_version,
    "update_pit": smartrace_events.update_pit,
    "update_event_status": smartrace_events.update_event_status,
    "update_controller_state": smartrace_events.update_controller_state,
}

async def smartrace_receive(connection:ClientConnection):
    async for message in connection:
        #print("### tablet2sensor ###")

        try:
            print(message)
            # convert message to dictionary
            message_json = json.loads(message)
            # emit signal if event is handled
            try:
                managed_events[message_json["type"]].emit(message_json["data"])
            except KeyError:
                print('skipped key error')


        except ConnectionClosed:
            print("smartrace_receive ConnectionClosed exception")
            #messages_queue2sensor.append(message)
            break

async def smartrace_connect(server:str, port:str) -> None:
    print('async smartrace_connect started')
    async for smartrace_socket in connect(f"ws://{server}:{port}"):
        try:
            smartrace_events.connection_successful.emit()

            _messages_queue.append('{"type": "controller_set", "data": {"controller_id": "X"}}')
            try:
                await asyncio.gather[
                    await smartrace_send(smartrace_socket),
                    await smartrace_receive(smartrace_socket)
                ]
            except TypeError:
                smartrace_events.connection_closed.emit()
                print("Server interrupted")
                pass

        except ConnectionClosed:
            smartrace_events.connection_closed.emit()
            continue
        await asyncio.sleep(1)
    print('async Smartrace lost ended')

