import re

def decode(m):
    m = str(hex(m))[2:].zfill(256)
    if m[0:2] != '02':
        return None

    msg = re.search('00(.*)', m).group(1)
    return msg