def phoneCall(min1, min2_10, min11, s):

    mins = 0

    rate = min1
    while s > 0:
        
        mins += 1
        
        if mins == 2:
            rate = min2_10
        elif mins > 10:
            rate = min11
        
        s -= rate
        if s < 0:
            mins -= 1
        
    return mins
