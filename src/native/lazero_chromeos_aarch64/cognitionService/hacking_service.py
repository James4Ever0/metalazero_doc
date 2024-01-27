import os
# just use plain nmap scanning.
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-d","--address",type=str,default="127.0.0.1",help="address to check")
cmd = lambda ip: "nmap {}".format(ip)
args = parser.parse_args()
os.system(cmd(args.address))
