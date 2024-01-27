import shellConnect as Sc

# to represent how you type these words? type it exactly according to what you've done in the past?
# we want it to learn anything from this process.
import time as T
while True:
    Sc.restart()
    Sc.inputs("hello world")
    T.sleep(1)
    content = Sc.display()
    print(content)
