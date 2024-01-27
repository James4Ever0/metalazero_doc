import sys
sys.path.append("../tools")

from twisted_template import TwistedProcess as TP

cmd="su"

import time
wait=lambda:time.sleep(1)

tp=TP([cmd])
for _ in range(5):
    tp.write(b'input text "123"\n')
    wait()
    print(tp.read(blocking=False))
