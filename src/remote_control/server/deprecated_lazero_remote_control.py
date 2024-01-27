# websocket screen cast?
# or just some normal requests.
from flask import Flask, request, Response

#homepage = ""
def homepage():
    with open("deprecated_index.html", "r") as f:
        return f.read()

import pyautogui
import mss
import threading
import traceback
# the monitor is just the screen position.
# shall one set the refresh rate manually.
from PIL import Image
from io import BytesIO
import time
framerate=10
current_shot = None
import copy
def takeshots():
    global current_shot, framerate
    standard_sleep_time = 1/framerate
    sleep_time = standard_sleep_time
    this_time, current_time = 0, 0
    check_loop = 5
    check_base = 0
    # you shall dynamically change the sleep time.
    try:
        with mss.mss() as mss_instance:
            monitor = mss_instance.monitors[1]
            while True:
#                check this shit every 5 shots.
                if check_base % check_loop == 0:
                    this_time = time.time()
                shot = mss_instance.grab(monitor)
                img = Image.frombytes("RGB", shot.size, shot.bgra, "raw", "BGRX")
                with BytesIO() as f:
                    img.save(f,format="JPEG")
                    image_jpg_bytes = f.getvalue()
                    current_shot = copy.copy(image_jpg_bytes)
#                print(shot,type(shot),dir(shot))
                if check_base % check_loop == 0:
                    current_time = time.time()
                    time_delta = current_time - this_time
                    if time_delta > standard_sleep_time:
                        sleep_time = 0
                    else:
                        sleep_time = standard_sleep_time - time_delta
                time.sleep(sleep_time)
                check_base += 1
                check_base %= check_loop
    except:
        traceback.print_exc()
        time.sleep(1)

screenshot_thread = threading.Thread(target=takeshots,daemon=True)
screenshot_thread.start()
app = Flask(__name__)


@app.route("/screenshot/<timestamp>.jpg")
def screenshot(timestamp):
    global current_shot
    shot = current_shot
    return Response(shot,mimetype="image/jpeg")

import lazero_mouse
import lazero_keyboard

@app.route("/mouse",methods=["POST"])
def mouse():
    body = request.get_json()
    try:
        _type = body["type"]
        if _type == "reset":
            lazero_mouse.reset_mouse()
        elif _type == "click":
            button = body["button"]
            lazero_mouse.click(button=button)
        elif _type == "doubleClick":
            button = body["button"]
            lazero_mouse.doubleClick(button=button)
        elif _type == "mouseDown":
            lazero_mouse.mouseDown()
        elif _type == "mouseUp":
            lazero_mouse.mouseUp()
        elif _type == "mouseMove":
            deltaX = body["deltaX"]
            deltaY = body["deltaY"]
            lazero_mouse.mouseMove(deltaX,deltaY)
        else:
            return "Unsupported mouse request type: {}".format(_type)
    #print("mouse request:",[request.values.get(x) for x in ["deltaX","deltaY"]])
        return "Mouse Request Accepted."
    except:
        traceback.print_exc()
        return "Error when performing mouse request."

@app.route("/keyboard",methods=["POST"])
def keyboard():
    body = request.get_json()
    print(body)
    try:
        _type = body["type"]
        if _type == "reset":
            lazero_keyboard.reset_keyboard()
        elif _type == "keyDowb":
            key = body["key"]
            key = lazero_keyboard.translate(key)
            lazero_keyboard.keyDown(key)
        elif _type == "keyUp":
            key = body["key"]
            key = lazero_keyboard.translate(key)
            lazero_keyboard.keyUp(key)
        else:
            return "Unsupported keyboard request type: {}".format(_type)
    #print("keyboard request:",[request.values.get(x) for x in ["character","modifier"]])
        return "Keyboard Request Accepted."
    except:
        traceback.print_exc()
        return "Error when performing keyboard request."

@app.route("/")
def index():
    #global homepage
    return homepage()

host, port = "0.0.0.0", 14986
if __name__ == "__main__":
    app.run(host=host,port=port)
