# High level usage using `spawn`
from winpty import PtyProcess
import time
# the only thing that's left is for a cross-platform twisted implementation.
proc = PtyProcess.spawn('cmd')
# proc = PtyProcess.spawn('python36')
proc.write('print("hello, world!")\r\n')
# proc.write('exit()\r\n')
# too quick.
# while proc.isalive():
# so it is time to do some hosting, convert terminal sequence into real stuff?
# or fuck it.
T=-5
while T<0:
    print("reading",proc.read())# this is blocking.
    # actually can read faster.
    T+=1
    time.sleep(0.5)
# print(dir(proc))
# ['__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_server', '_thread', '_winsize', 'argv', 'close', 'closed', 'decoder', 'delayafterclose', 'delayafterterminate',
# 'env', 'eof', 'exitstatus', 'fd', 'fileno', 'fileobj', 'flag_eof', 'flush', 'getwinsize', 'isalive', 'isatty', 'kill', 'launch_dir', 'pid', 'pty', 'read', 'read_blocking', 'readline', 'sendcontrol', 'sendeof', 'sendintr', 'setwinsize', 'spawn', 'terminate', 'wait', 'write']
# check for read screen.
# proc.close(force=True) <- SIGINT first.
proc.terminate()
# must close.
# End winpty-agent process
del proc
exit(0)
# however, pty related things are not about stderr/stdout distinguishing. 
# they are merged.
# yawinpty has different io. check for another pty equivalent.
# https://pypi.org/project/yawinpty/
# https://asciinema.org/ -> replaying session or reviewing it?
# replace ;; with ;.
# multiple errors, i suppose.