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
#b="Content-Length: {}".format(l)
b="""Content-Length: {}\r\n
Content-Type: application/vscode-jsonrpc; charset=utf8\r\n""".format(l)
#print(b,end="")
#print(c+"\x04")
for x in range(50):
    print(c,end="\r\n")
#    print("")
