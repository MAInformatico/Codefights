def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    result = ' '
    if (yourLeft == friendsLeft and yourRight == friendsRight) or (yourLeft == friendsRight and yourRight == friendsLeft):
        result = True    
    else:
        result = False

    return result
