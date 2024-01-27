import json
import os
codename = ".local_name_resolution.json"
# if in return true.
def checkin(uuid,ip,data):
    r = uuid in data.keys()
    if not r:
        return r
    else:
        r = (data[uuid] == ip)
        return not r

def get_table():
    if os.path.exists(codename):
        return json.loads(open(codename,"r").read())
    else:
        with open(codename,"w+") as f:
            f.write(json.dumps({}))
        return get_table()

def set_table(uuid,ip):
    table = get_table()
    result = checkin(uuid,ip,table)
    if not result:
        table.update({uuid:{"ip":ip}})
        with open(codename,"w+") as f:
            f.write(json.dumps(table))
    return result
