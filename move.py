import asyncio
import json

import websockets
from pynput.mouse import Controller
from screeninfo import get_monitors

mouse = Controller()
monitor = get_monitors()[0]  # Assumes a single monitor setup
screen_width = monitor.width
screen_height = monitor.height


def move_cursor(x, y):
    mouse.position = (x, y)  # Directly set the cursor position
    print(x, y)


# WebSocket handler
async def move_cursor_server(websocket):
    print(f"Client connected: {websocket.remote_address}")

    try:
        async for message in websocket:
            # Parse JSON message
            data = json.loads(message)
            x, y = data['x'], data['y']
            newX = int(x * screen_width / 300)
            newY = int(y * screen_height / 400)
            move_cursor(newX, newY)
    except websockets.exceptions.ConnectionClosed:
        print(f"Client disconnected: {websocket.remote_address}")
    except Exception as e:
        print(f"Error: {e}")


# Start the WebSocket server
if __name__ == "__main__":
    server_address = "192.168.1.14"  # Replace with your server IP
    server_port = 8765
    start_server = websockets.serve(move_cursor_server, server_address, server_port)

    print(f"Server running on ws://{server_address}:{server_port}")
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
