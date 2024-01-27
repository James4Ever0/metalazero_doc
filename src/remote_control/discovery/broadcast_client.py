from socket import *
from generate_uuid import get_uuid
# with different ip?
host = "255.255.255.255"
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--ip",type=str,default= "255.255.255.255")
    args = parser.parse_args()
    host = args.ip
def reply_info(address=host):
    uuid = get_uuid()
    message = "[LNRR]: {}".format(uuid).encode("utf-8")
    port = 30000
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    s.sendto(message,(address,port))

if __name__ == "__main__":
    reply_info()
