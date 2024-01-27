import traceback
import threading
import os

# shall provide common hotkeys in chromebook keyboard mappings.
import platform
system = platform.system()
keyset = set()
def win_meta(key):
    return key.replace("meta","win")


def translate(key):
    if key in ["meta","metaleft","metaright"]:
        if system == "Darwin":
            return "command"
        return win_meta(key)
    return key

def press(key):
    cmd = "python3 -c \"import pyautogui;pyautogui.press('{}')\"".format(key.replace("'","\\'"))
    threading.Thread(target=os.system,args=(cmd,),daemon=True).start()
    
    # what shall be included in these keys?
"""
def hotkey(keys):
    target = keys["modifier"]+keys["char"]
    pyautogui.hotkey(*target)
"""
def keyDown(key):
    global keyset
    keyset.add(key)
    cmd = "python3 -c \"import pyautogui;pyautogui.keyDown('{}')\"".format(key.replace("'","\\'"))
    threading.Thread(target=os.system,args=(cmd,),daemon=True).start()

def keyUp(key):
    cmd = "python3 -c \"import pyautogui;pyautogui.keyUp('{}')\"".format(key.replace("'","\\'"))
    threading.Thread(target=os.system,args=(cmd,),daemon=True).start()
    keyset.remove(key)
"""
def write(key):
    pyautogui.write(key)# able to type uppercase letters?
"""
def reset_keyboard():
    for x in keyset:
#        threading.Thread(target=keyUp,args=(x,),daemon=True).start()
        try:
            keyUp(x)
        except:
            traceback.print_exc()
    return

if __name__ == "__main__":
    print("KEYBOARD_KEYS",pyautogui.KEYBOARD_KEYS)
    print("KEY_NAMES",pyautogui.KEY_NAMES)
