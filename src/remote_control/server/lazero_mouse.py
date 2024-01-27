import traceback
import threading
import os

def mouseMove(deltaX, deltaY):
    print("request move:", deltaX, deltaY)
    print(type(deltaX))
    try:
        cmd = "python3 -c \"import pyautogui; pyautogui.moveRel({},{})\"".format(deltaX, deltaY)
        threading.Thread(target=os.system,args=(cmd,),daemon=True).start()
    except:
        traceback.print_exc()

def mouseDown():
    cmd = "python3 -c \"import pyautogui; pyautogui.mouseDown()\""    
    threading.Thread(target=os.system,args=(cmd,),daemon=True).start()

def mouseUp():
    cmd = "python3 -c \"import pyautogui; pyautogui.mouseUp()\""    
    threading.Thread(target=os.system,args=(cmd,),daemon=True).start()

def click(button="left"):
    cmd = "python3 -c \"import pyautogui; pyautogui.click(button='{}')\"".format(button)
    threading.Thread(target=os.system,args=(cmd,),daemon=True).start()
"""
def leftClick():
    pyautogui.leftClick()

def rightClick():
    pyautogui.rightClick()
"""
def reset_mouse():
    mouseUp()
    return
def doubleClick(button="left"):
    cmd = "python3 -c \"import pyautogui; pyautogui.doubleClick(button='{}')\"".format(button)
    threading.Thread(target=os.system,args=(cmd,),daemon=True).start()
