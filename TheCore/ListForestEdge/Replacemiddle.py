def replaceMiddle(arr):
    if len(arr)%2 != 0:
        return arr
    else:
        middle_index = len(arr) // 2
        middle = arr [middle_index] + arr[middle_index - 1]
        return arr[:middle_index - 1] + [middle] + arr[middle_index + 1:]      
