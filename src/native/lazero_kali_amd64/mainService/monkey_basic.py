import pyautogui
import random
import time

def getMouse():
    x,y = pyautogui.size()
    x0, y0 = random.randint(0,x), random.randint(0,y)
    print("new location:",x0,y0)
    return x0, y0

def mouseMove(delay=0.2):
    x0,y0 = getMouse()
    pyautogui.moveTo(x0,y0,duration=delay)

def mouseClick(delay=0.2):
    pyautogui.mouseDown()
    time.sleep(delay)
    pyautogui.mouseUp()

def mouseDrag(delay=0.2):
    x0, y0 = getMouse()
    pyautogui.dragTo(x0,y0,duration=delay)

def keyToggle(delay=0.2):
    keys = pyautogui.KEYBOARD_KEYS
    k = random.choice(keys)
    print("pressing key:",k)
    pyautogui.keyDown(k)
    time.sleep(delay)
    pyautogui.keyUp(k)

def hotkey(delay=0.2,keys_range=(2,5)):
    keys = pyautogui.KEYBOARD_KEYS
    k = []
    random.sample(keys,random.randint(*keys_range))
    print("pressing hotkeys:",*k)
    pyautogui.hotkey(*k,interval=delay/len(k))

def execute():
    functions = [mouseDrag, mouseMove, mouseClick, keyToggle, hotkey]
    f = random.choice(functions)
    print("executing function:",f.__name__)
    f()

if __name__ == "__main__":
    while True:
        execute()
