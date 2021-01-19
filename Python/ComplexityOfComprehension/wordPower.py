def wordPower(word):
    num = {y: x+1 for x, y in enumerate('abcdefghijklmnopqrstuvwxyz')}
    return sum([num[ch] for ch in word])
