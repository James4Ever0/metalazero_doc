import io
import threading
import time

target = io.BytesIO()

def read_target():
    while True:
        bytes_ = target.read()
        print("bytes:", bytes_)
def check_target():
    print("buffer:",target.getbuffer())
    print("value:",target.getvalue())
print(dir(target))
# this is first.
target.write(b"abc")
values = target.read1()
print(values)
# nothing could be read.
print(target.tell())
# this is the cursor, we can reset it of course.
target.seek(0)
print(target.read())
target.write(b"hello")
print(target.tell())
target.seek(0)
print(target.read())
buffer0 = target.getbuffer()
buffer0 = b""
# so this fucking works or not?
# do we really read the shit after all?
print(target.read())
print(target.getvalue())
target.truncate()
print(target.getvalue())
