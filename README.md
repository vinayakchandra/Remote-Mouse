# Remote Mouse Tracker

A web-based application that allows users to control the mouse cursor remotely and simulate left and right clicks. The
application uses `Flask` for the backend, `WebSockets` for real-time communication, and HTML with JavaScript on the
frontend to track mouse movements and handle click events.

## Features

- Track and move the mouse cursor remotely based on user input.
- Simulate left and right mouse clicks through buttons on the web interface.
- Real-time communication between the web interface and Python backend using WebSockets.

## API Endpoints

| Method | Endpoint                | Description                                                    |
|--------|-------------------------|----------------------------------------------------------------|
| `GET`  | `/`                     | Renders the main `HTML` page with the mouse tracker interface. | 
| `GET`  | `/left_click`           | Simulates a left-click.                                        | 
| `GET`  | `/right_click`          | Simulates a right-click.                                       |
| `WS`   | `ws://<server_ip>:8765` | WebSocket connection for real-time mouse position updates.     | 

You can install the necessary Python libraries using `pip`:

```bash
  pip install -r requirements.txt
```


## Flask Backend

The `Flask` application serves the HTML page and has two endpoints:
`/`: Renders the main page.
`/left_click` and `/right_click`: Simulate left and right mouse clicks using the `pynput` library.

## WebSocket Server

The `WebSocket` server listens for incoming messages that contain `x` and `y` coordinates, then adjusts the mouse position
based on those values. It resizes the coordinates to match the system's screen resolution.

## Frontend (HTML + JavaScript)

The frontend listens for mouse movements inside the tracker box and sends the coordinates to the WebSocket server.
It also sends requests to the Flask server to simulate left and right clicks when the corresponding buttons are pressed.
`http://<server_ip>:5000`

