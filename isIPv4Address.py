def isIPv4Address(inputString):
    if len(inputString.split(".")) != 4:
        return False
    else:
        data = inputString.split(".")
        for i in data:
            if i == "" or i.isdigit() == False:
                return False
            if int(i)<0 or int(i)>255:
                return False
        return True
