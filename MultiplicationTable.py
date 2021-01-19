def multiplicationTable(n):
    return [[i for i in range(j,j*n+1,j)] for j in range(1,n+1)]
