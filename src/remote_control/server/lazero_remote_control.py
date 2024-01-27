# websocket screen cast?
# or just some normal requests.
from flask import Flask, request, Response, render_template

#homepage = ""
def homepage():
    with open("index.html", "r") as f:
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

lock = threading.Event()
lock.clear()

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
                lock.set()
                time.sleep(sleep_time)
                check_base += 1
                check_base %= check_loop
    except:
        traceback.print_exc()
        time.sleep(1)

screenshot_thread = threading.Thread(target=takeshots,daemon=True)
screenshot_thread.start()
app = Flask(__name__, template_folder="./")


@app.route("/mouse",methods=["POST"])
def mouse():
    print("mouse request:",[request.values.get(x) for x in ["deltaX","deltaY"]])
    return

@app.route("/keyboard",methods=["POST"])
def keyboard():
    print("keyboard request:",[request.values.get(x) for x in ["character","modifier"]])
    return

def gen():
    global current_shot
    while True:
        lock.wait()
        frame = copy.copy(current_shot)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route("/video_feed")
def video_feed():
    return Response(gen(),
                mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/")
def index():
    #global homepage
    return render_template("index.html")

host, port = "0.0.0.0", 14986
if __name__ == "__main__":
    app.run(host=host,port=port)
