import io
import threading

# shall we use os.pipe instead?

class BytesMemPipe:
    def __init__(self):
        self.BytesIO = io.BytesIO()
        self.write_lock = threading.Event()
        self.read_lock = threading.Event()
        self.write_lock.clear()
        self.read_lock.clear()
    def write(self, _bytes):
        self.BytesIO.write(_bytes)
        self.read_flush()
        self.write_lock.wait()
        self.BytesIO = io.BytesIO()
        return len(_bytes)
    def read(self):
        self.write_flush()
        self.read_lock.wait()
        target = self.BytesIO.getvalue()
        return target
    def flush(self):
        return
    def read_flush(self):
        self.read_lock.set()
        self.read_lock.clear()
    def write_flush(self):
        self.write_lock.set()
        self.write_lock.clear()
