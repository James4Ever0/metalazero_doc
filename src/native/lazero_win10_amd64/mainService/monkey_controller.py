# this is the pyautogui version of the monkey, providing our basic data for training.
# advanced algos will be possible only if we have the data.
# we go dumb first.
import pyautogui
import random
# but first we must fuzz around the code.
targets=dir(pyautogui)
while True:
    t = random.choice(targets)
    cmd = "pyautogui.{}".format(t)
    print("executing command:",cmd)
    r = eval(cmd)
    print("result:",r)
    # let me know more about the controller.
    # we do not know the shit yet.
