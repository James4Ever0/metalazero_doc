from pynput.keyboard import Key, Listener
#        socket.send("client message to server1")
import time as T
# so doing self-looping?
from sys import path as SP

SP.append("../tools")
from stackMe import queue as Q

def GT():
    return T.time()

def on_press(key,queue=None,keycode_only=True):
    typecode = str(type(key))
    key_str = str(key)
#    print(dir(key))
    print("LOGGING:",key_str,typecode)
    if keycode_only:
        if "KeyCode" in typecode:
#            print("passed 1")
            if len(key.char) == 1:
#                print("passed 2")
                queue.queue((key.char,GT()))
    else:
        queue.queue((key_str,GT()))
    #print(str(key),typecode)

def log_to_queue(queue,keycode_only=True):
    assert type(queue) == type(Q(0))
    on_press2 = lambda key: on_press(key,queue=queue,keycode_only=keycode_only)
    with Listener(on_press=on_press2) as listener:
        try:
            listener.join()
        except:
            pass
