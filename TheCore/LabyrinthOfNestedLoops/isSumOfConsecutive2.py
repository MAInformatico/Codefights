def isSumOfConsecutive2(n):
    result = 0
    for i in range(1,n//2+1):
        aux = 0
        j = i
        while aux < n:
            aux += j
            j += 1
        if aux == n: result += 1    
    return result
