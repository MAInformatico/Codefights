def arrayMaximalAdjacentDifference(inputArray):
    maxdiff = 0
    for i in range(len(inputArray)):
        if i<len(inputArray)-1 and abs(inputArray[i] - inputArray[i+1]) > maxdiff :
            maxdiff = abs(inputArray[i] - inputArray[i+1])
    return maxdiff
