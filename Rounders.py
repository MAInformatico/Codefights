def rounders(n):
    leng = len(str(n))
    mag = leng - 1
    for i in range(leng - 1):
        n = int((n / 10) + 0.5)
    return n * (10 ** mag)
