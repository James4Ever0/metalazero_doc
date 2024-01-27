import os
import uuid

def generate():
    return str(uuid.uuid4())

def set_uuid():
    with open(".local_uuid","w+") as f:
        f.write(generate())

def get_uuid():
    if os.path.exists(".local_uuid"):
        return open(".local_uuid","r").read()
    else:
        set_uuid()
        return get_uuid()
