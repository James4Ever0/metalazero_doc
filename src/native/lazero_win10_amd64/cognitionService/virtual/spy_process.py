import sys

while True:
    m = sys.stdin.buffer.readline()
    # print(m)
    sys.stdout.buffer.write(m)
    # sys.stdout.buffer.write(bytearray("hello world\n",encoding='utf-8'))
    sys.stdout.buffer.flush()
        # print(chr(line),end="",file=sys.stdout)
        # print(line)
    # sys.stdout.buffer.write(bytearray([line]))