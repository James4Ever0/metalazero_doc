import uuid

def ufname(ext):
    assert len(ext.replace(".",""))>0
    prefix = str(uuid.uuid4())
    if ext.startswith("."):
        return prefix+ext
    else:
        return ".".join([prefix,ext])
