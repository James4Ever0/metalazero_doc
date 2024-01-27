import sys

bytebuffer = bytearray()
for x in sys.stdin.buffer.read():
    bytebuffer.append(x)
string = bytes(bytebuffer).decode("utf-8")
#print(string,end="")
import json
target = json.loads(string)
print(target)
