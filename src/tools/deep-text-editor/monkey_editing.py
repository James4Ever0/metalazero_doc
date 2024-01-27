from editor import editor
import random
import time
def gen_str():
    return "".join([chr(random.randint(0,200)) for x in range(random.randint(2,5))])

while True:
    print("starting over.")
    insert=lambda: e.insert(gen_str())
    replace=lambda: e.replace(gen_str())
    copy=lambda: e.copy(gen_str())
    paste=lambda: e.paste()
    forward=lambda: e.forward(random.randint(2,5))
    backward=lambda: e.backward(random.randint(2,5))
    delete=lambda: e.delete(random.randint(2,5))
    backspace=lambda: e.backspace(random.randint(2,5))
    e=editor("".join([gen_str() for x in range(5)]))
    ops=[insert,replace,copy,paste,backspace,delete,forward,backward]
    for _ in range(500):
        random.choice(ops)()
        print("current state:",e.content,e.position)
        time.sleep(0.01)
