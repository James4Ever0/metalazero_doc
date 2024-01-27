msg="""{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "shutdown", 
	"params": {}
}"""
l=len(msg)
header="""Content-Length: {}\r\n
\r\n""".format(l)
wr=header+msg
import time
while True:
    print(wr,end="\r\n")
    time.sleep(1)

