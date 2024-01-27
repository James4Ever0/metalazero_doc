#a="length: 256"
import os
rpath=os.environ["PWD"]
import json
c={}
c.update({"jsonrpc":"2.0"})
c.update({"id":1})
c.update({"method":"initialize","params":{"rootPath":rpath,"capabilities":[]}})
c=json.dumps(c)
l=len(c)
b="Content-Length: {}".format(l)

print("")
#print(b)
print("")
print(c+"")
#print(c+"\x04")
print("")
