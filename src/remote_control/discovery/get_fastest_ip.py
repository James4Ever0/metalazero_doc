from pythonping import ping
import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f","--file",type=str,required=True)
parser.add_argument("-u","--uuid",type=str,required=True)
args = parser.parse_args()
target_file = args.file
target_uuid = args.uuid
with open(target_file,"r") as f:
    lists = []
    for line in f:
        content = json.loads(line)
        if content["text"] == target_uuid:
            lists.append(content["ip"])
# not permitted. shit.
import random
print(random.choice(lists))
"""
for ip in lists:
    response_list = ping(ip, size=40, count=10)
    delay = ip.rtt_avg_ms
    results.append((ip,delay))

for ip, delay in sorted(results, key=lambda x: x[1]):
    print(ip)
    break
"""
