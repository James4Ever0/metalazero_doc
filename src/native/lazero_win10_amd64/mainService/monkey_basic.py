import pyautogui
import random
import time

def mouseMove(delay=0.2):
    x,y = pyautogui.size()
    x0, y0 = random.randint(0,x), random.randint(0,y)
    print("new location:",x0,y0)
    pyautogui.moveTo(x0,y0,duration=delay)

def mouseClick(delay=0.2):
    pyautogui.mouseDown()
    time.sleep(delay)
    pyautogui.mouseUp()

def keyToggle(delay=0.2):
    keys = pyautogui.KEYBOARD_KEYS
    k = random.choice(keys)
    print("pressing key:",k)
    pyautogui.keyDown(k)
    time.sleep(delay)
    pyautogui.keyUp(k)

def execute():
    functions = [mouseMove, mouseClick, keyToggle]
    f = random.choice(functions)
    print("executing function:",f.__name__)
    f()

if __name__ == "__main__":
    while True:
        execute()
