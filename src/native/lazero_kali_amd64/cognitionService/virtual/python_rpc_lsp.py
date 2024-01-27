cnt="""\r\n
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "$/solargraph/restartServer",
	"params": {
        "random":true
	}
}
"""
#import time
while True:
    #time.sleep(1)
    print(cnt,end="\r\n",flush=True)
