from telnetlib import Telnet
t = Telnet("localhost",10000)
t.write(b"hello world\n")
c=t.read_until(b"\n")
print(c)
