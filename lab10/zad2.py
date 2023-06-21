from websocket import WebSocketApp

def on_open(ws):
    print("Connection is opened.")
    message = "Hello, WebSocket!"
    if len(message.encode('utf-8')) <= 125:  # Ensure the message is not longer than 125 bytes
        ws.send(message)
    else:
        print("Message is too long.")

def on_message(ws, message):
    print(f"Received message: {message}")

def on_close(ws):
    print("Connection is closed.")

def on_error(ws, error):
    print(f"Error occurred: {error}")


address = "ws://echo.websocket.org"

ws = WebSocketApp(address, 
                  on_open=on_open,
                  on_message=on_message,
                  on_close=on_close,
                  on_error=on_error)

ws.run_forever()
