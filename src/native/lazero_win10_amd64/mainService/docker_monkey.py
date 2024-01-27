# without monkey typers we cannot really say that we are making any progress with this shitty computer.
# we are not familar with this shit though!
import winpexpect as pexpect
import threading
import random
import time
# maybe you need winpexpect.
# we shall start shits from simple rules.
# anything unpredictable that could also last forever.
p = pexpect.spawn("docker run --rm --read-only -i alpine")
def read_me():
    while True:
        content = p.readline()
        print("content:\n",content)

#print(dir(p))
threading.Thread(target=read_me,daemon=True).start()
delay=0.2
while True:
    payloads = ["whoami","pwd","ls"]
    time.sleep(delay)
    target = random.choice(payloads)
    print("sending command:",target)
    p.sendline(target)
