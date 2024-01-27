from twisted.internet import protocol, reactor
import time
# import sys
import threading
# password is a must here. not kidding.
import os

def isWINDOWS():
    return os.name == "nt"

class Reader:
    def __init__(self):
        self.event = threading.Event()
        self.event.clear()
        self.buffer = bytearray(b'')
    def clear(self):
        self.event.clear()
    def set(self):
        self.event.set()
    def write(self,_bytes,blocking=True):
        assert type(_bytes) == bytes
        if blocking:
            if len(_bytes) == 0:
                return
        self.buffer.extend(_bytes)
        self.event.set()
    def read(self,blocking=True):
        if blocking:
            self.event.wait()
            self.event.clear()
        _bytes = bytes(self.buffer)
        self.buffer.clear()
        return _bytes
    def clear(self):
        self.buffer.clear()

class MyPP(protocol.ProcessProtocol):
    def __init__(self,reader):
        super().__init__()
        self.reader = reader

    def connectionMade(self):
        CM = lambda: print("\n[Connection Made]\n")
        CM()
        # reactor.callLater(1.0, CM)

    def write(self, a):
        # binary.
        assert type(a) == bytes
        self.transport.write(a)

    def processExited(self, reason):
        print("processExited, status %s" % (reason.value.exitCode,))

    def outReceived(self, data):
        self.reader.write(data)

    def errReceived(self, data):
        self.reader.write(data)

import sys
sys.path.append("..\\tools")
from where import where

class TwistedProcess:
    # def __init__(self,command=["cmd.exe"],usePTY=True):
    def __init__(self,command=["cmd"],usePTY=True,env=dict(os.environ), path=None,autolocate=True):
        assert type(command) == list and len(command)>0
        if isWINDOWS():
            print("System is Windows. Forced to use non-PTY mode.")
            usePTY = False
    # how to kill this process?
        reader = Reader()
        self.reader = reader
        pp = MyPP(reader)
        def theFunc(a):
            try:
                a.run()
            except:
                pass
        # process = reactor.spawnProcess(pp, command[0], command, usePTY=usePTY)
        executable = command[0]
        if autolocate:
            if not os.path.isabs(executable):
                executable = where(executable)[0]
        process = reactor.spawnProcess(pp, executable, command, env=env, path=path, usePTY=usePTY)
        # print(dir(process))
        # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__implemented__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__providedBy__', '__provides__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_addPollableResource', '_callProcessExited', '_checkPollingState', '_currentTimeout', '_getReason', '_pause', '_paused', '_pollEvent', '_pollTimer', '_reschedule', '_resources', '_startPolling', '_stopPolling', '_unpause', 'closeChildFD', 'closeStderr', 'closeStdin', 'closeStdout', 'closedNotifies', 'connectionLostNotify', 'errConnectionLost', 'hProcess', 'hStderrR', 'hStdinW', 'hStdoutR', 'hThread', 'inConnectionLost', 'loseConnection', 'lostProcess', 'maybeCallProcessEnded', 'outConnectionLost', 'pauseProducing', 'pid', 'processEnded', 'proto', 'reactor', 'registerProducer', 'resumeProducing', 'signalProcess', 'status', 'stderr', 'stdin', 'stdout', 'stopProducing', 'unregisterProducer', 'write', 'writeSequence', 'writeToChild']
        self.process=process
        self.pp = pp
        p = threading.Thread(target=theFunc,args=(reactor,)) # pause the reactor?
        p.setDaemon(True)
        p.start() # not RUN!
    def write(self,text):
        assert type(text) == bytes
        self.pp.write(text)
    def read(self,blocking=True):
        return self.reader.read(blocking=blocking)
    def terminate(self):
        # usually not reusable. all will be deleted.
        self.reader.clear()
        pid = self.process.pid
        # try:
        #     self.process.closeStderr()
        #     self.process.closeStdin()
        #     self.process.closeStdout()
        #     # reactor.stop()
        # except:
        #     pass
        return pid
    def isalive(self):
        return self.process.processEnded