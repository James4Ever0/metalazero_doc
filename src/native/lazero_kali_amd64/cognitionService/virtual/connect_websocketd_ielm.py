import websocket

ws = websocket.WebSocket()
ws.connect("ws://localhost:9999")
ws.send("(print \"Hello, Server\")")
#print(ws.timeout) #none. block forever.
ws.settimeout(2)
try:
    while True:
        print(ws.recv())
except:
    print("timed out")
    ws.close()
