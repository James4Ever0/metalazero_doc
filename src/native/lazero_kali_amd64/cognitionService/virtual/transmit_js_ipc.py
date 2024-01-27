import sys
while True:
    cmd=""
    for line in sys.stdin.buffer.readline():
        cmd+=chr(line)
        print("reading:",line)
        print("buffer:",cmd)
    print("next round?")
