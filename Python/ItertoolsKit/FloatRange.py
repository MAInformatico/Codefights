from itertools import count, takewhile

def floatRange(start, stop, step):
    gen = takewhile(lambda i: i < stop, count(start,step))
    return list(gen)
