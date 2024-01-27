from editor import editor
import random
import time
def gen_str():
    return "".join([chr(random.randint(0,200)) for x in range(random.randint(1,2))])

def monkey(content):
    e=editor(content=content)
    insert=lambda: e.insert(gen_str())
    replace=lambda: e.replace(gen_str())
    copy=lambda: e.copy(gen_str())
    paste=lambda: e.paste()
    forward=lambda: e.forward(random.randint(1,2))
    backward=lambda: e.backward(random.randint(1,2))
    delete=lambda: e.delete(random.randint(1,2))
    backspace=lambda: e.backspace(random.randint(1,2))
    ops=[insert,replace,copy,paste,backspace,delete,forward,backward]
    for _ in range(15):
        random.choice(ops)()
    return e.content
