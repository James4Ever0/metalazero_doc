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
target.write(b"abc")
check_target()
target.flush()
check_target()
values = target.read1()
print(values)
# nothing could be read.
print(target.tell())
# this is the cursor, we can reset it of course.
target.seek(0)
print(target.read())
