#!/usr/bin/env python3

import asyncio
import websockets

async def server(websocket, path):
    # Get received data from websocket
#    data = await websocket.recv()
    await websocket.send("thanks for whatever shit you have sent to me.")
    await websocket.send("thanks for whatever shit you have sent to me.")
    await websocket.send("thanks for whatever shit you have sent to me.")
    # Send response back to client to acknowledge receiving message
#    await websocket.send("Thanks for your message: " + data)

# Create websocket server
start_server = websockets.serve(server, "localhost", 9998)

# Start and run websocket server forever
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
