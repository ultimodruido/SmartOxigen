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

from websockets.asyncio.client import connect, ClientConnection
from websockets.exceptions import ConnectionClosed

from .smartrace_events import smartrace_events

_messages_queue = list()

async def smartrace_send(connection:ClientConnection):
    pass

async def smartrace_receive(connection:ClientConnection):
    async for message in connection:
        #print("### tablet2sensor ###")

        try:
            print(message)

        except ConnectionClosed:
            print("smartrace_receive ConnectionClosed exception")
            #messages_queue2sensor.append(message)
            break

async def smartrace_connect(server:str, port:str) -> None:
    print('async smartrace_connect started')
    async for smartrace_socket in connect(f"ws://{server}:{port}"):
        try:
            smartrace_events.connection_successful.emit()

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

