import websocket

def on_message(wsapp, text):
    print(text)
# still a client?
wsapp=websocket.WebSocketApp("ws://localhost:9998",on_message=on_message)
wsapp.run_forever()
#print("shit?")
