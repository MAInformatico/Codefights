def buildPalindrome(st):
    if st == st[::-1]:
        return st
    else:
        index = 0
        auxst = st[index:]
        while auxst != auxst[::-1]:
            index += 1
            auxst = st[index:]
        return st + st[index - 1::-1] 
