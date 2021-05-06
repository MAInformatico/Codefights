from itertools import cycle

def cyclicName(name, n):
    gen = (i for i in cycle(name))
    res = [next(gen) for _ in range(n)]
    return ''.join(res)
