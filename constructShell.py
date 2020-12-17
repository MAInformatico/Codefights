def constructShell(n):
    return [[0 for j in range(2*n-i)] if i > n else [0]*i  for i in range(1, 2*n)]
