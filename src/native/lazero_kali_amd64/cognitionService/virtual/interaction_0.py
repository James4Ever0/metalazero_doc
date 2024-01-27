import shellConnect as Sc
# we can use multiple methods simutaneously.

# to represent how you type these words? type it exactly according to what you've done in the past?
# we want it to learn anything from this process.
import time as T
# let's mutate!

class Processor:
    def __init__(self):
        pass
    def get(self):
        return "Hello world"
    def set(self,content):
        return

p = Processor()
while True:
    Sc.restart()
    inp = p.get()
    Sc.inputs(inp)
    T.sleep(1)
    content = Sc.display()
    p.set(content)
    print(content)
