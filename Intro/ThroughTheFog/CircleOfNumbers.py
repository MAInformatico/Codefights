def circleOfNumbers(n, firstNumber):
    v = 0
    if n/2 > firstNumber:
        v = int(firstNumber + n/2)
    else:
        v = int(firstNumber- n/2)
    return v
