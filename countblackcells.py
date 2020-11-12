def gcd(value1, value2):
    while value2:
        value1, value2 = value2, value1%value2
    return value1

def countBlackCells(n, m):
    return n + m + gcd(n,m) - 2  
