from socket import *
from generate_uuid import get_uuid
from update_local_name_resolution_table import set_table
from broadcast_client import reply_info
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-o","--override",action="store_true",help="overriding the uniq-filtering feature")
parser.add_argument("-u","--unique",help="number of unique collections to be collected before close (not including self", type=int, default = 0)
#message = "lazero name resolution request
args = parser.parse_args()
# shall be updating the name resolution table.
# you will refer to the unique identifier once and ever.
# to translate the thing.
def parse_uuid(string):
    prefix = "[LNRR]: "
    if string.startswith(prefix):
        return string.replace(prefix,"")
    return False
# i really want to know that what is the best way to do this job, but let me say it again.
port = 30000
host = ""
uuid = get_uuid()
s = socket(AF_INET, SOCK_DGRAM)
s.bind((host,port))
self_uuid = get_uuid()
assert args.unique >= 0
unique = args.unique
override = args.override
limit = unique
countdown = unique > 0
while True:
    m = s.recvfrom(1024)
    print("message received:",m)
    # tuple.
    ip_location = m[1][0]
    string = m[0].decode("utf-8")
    uuid = parse_uuid(string)
    result = set_table(uuid,ip_location)
    # not for once?
    def respond(unique=False):
        mark = " " if not unique else " unique "
        print("reply to{}message from {} at {}".format(mark,uuid,ip_location))
        reply_info(ip_location)
        # you shall reply the shit.
    if countdown:
        if limit > 0:
            if uuid != self_uuid:
                print("checking uuid:",uuid,self_uuid)
                respond(True)
                limit -= 1
        else:
            # exit the loop.
            break
        #check the limit, if exceeds then we exit.
    else:
        if not result or override:
            respond()
            # you have got the new shit! reply for gratitide.
    # try to check it once and for good?
    # if it is yourself then do not send shit? if inside then do not send shit.
#    print(type(m))
    # shall request fron this shit first.
#s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
#s.sendto(message,(host,port))
