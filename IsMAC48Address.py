import re
def isMAC48Address(inputString):
    p = re.compile(r'^([0-9A-F]{2}-){5}[0-9A-F]{2}$')
    if re.findall(p, inputString):
        return True
    else:
        return False
