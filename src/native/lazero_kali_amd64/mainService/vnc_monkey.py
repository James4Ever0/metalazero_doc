#import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-p","--passwd",type=str,required=True)
parser.add_argument("-a","--address","--add_argumentress",type=str,required=True)
args = parser.parse_args()

passwd = args.passwd
#passwd = passwd.encode()
address = args.address

from vncdotool import api
client = api.connect(address.replace(":","::"),password=passwd)
#tmp = lambda x: "vncdotool -s {} -p {} {}".format(address,passwd,x)
import random
import time
# that's called software testing? do you want to test me baby~
def mouseMove(delay=0.2):
    x,y = random.randint(0,1024),random.randint(0,768)
    client.mouseMove(x,y)
    print("moving to click at:",(x,y))
    time.sleep(delay/2)
    client.mousePress(1)
    time.sleep(delay/2)

def keyType(delay=0.2):
    t = "abcdefghijklmnopqrstuvwxyz"
    t+= t.upper()
    t+= "0123456789"
    t = [x for x in t]
    t = random.choice(t)
    print("pressing key:",t)
    client.keyPress(t)
    time.sleep(delay)

if __name__ == "__main__":
    fs = [keyType, mouseMove]
#    fs = [keyType]
    while True:
        f = random.choice(fs)
        f()
