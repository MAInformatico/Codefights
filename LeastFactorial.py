def leastFactorial(n):
    for i in range(n):
        if math.factorial(i)>=n:
            return math.factorial(i)
