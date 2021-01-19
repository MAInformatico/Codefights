def isSmooth(arr):
    result = False
    if arr[0] != arr[-1]:
        return result
    if len(arr)%2 == 0:
        middle = arr[len(arr) // 2] + arr[(len(arr) // 2) - 1]
    else:
        middle = arr[len(arr) // 2]        
        
    result = arr[0] == middle
    return result
