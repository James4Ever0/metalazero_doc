import pexpect
import time
import threading

from bytes_blocking import BytesMemPipe

logfile = BytesMemPipe()

child = pexpect.spawn("python3 sample_script.py", logfile=logfile)
#child = pexpect.spawn("python3 sample_script.py", logfile=logfile, use_poll=True )

def read_logfile():
    while True:
        print("logfile:",logfile.read())

threading.Thread(target=read_logfile,daemon=True).start()
# this is not transparent. 
# child.write_to_stdout=True
# this is a function.
# we shall have the lock here.

time.sleep(2)
print(dir(child))
print(type(child))
# you don't expect you get shit.
target = child.expect("lucky")
print(target)
time.sleep(2)
# stuck forever?
#child.sendline("123")
#child.sendeof()
child.write("123\r\n")
#child.flush()
# this is to clear the buffer?
#child.write("")
#child.flush()
#child.interact()
# the return is not right.
#child.expect(pexpect.EOF)
target = child.read()
print("read from target:", target)
# when you do this you shall not be doing other shits.
#child.read_nonblocking()
#child.expect("does not exist")
print(child.isalive())
print(child.isatty())
child.wait()
time.sleep(1)
# this is hackish enough? or not?
# i've got to say today's mission is about exporting all the data to my fucking directory, and then close all windows.
