def candles(candlesNumber, makeNew):    
    result = 0
    leftovers = 0
    while candlesNumber > 0:
        result += candlesNumber
        leftovers += candlesNumber
        candlesNumber = 0
        candlesNumber = leftovers // makeNew
        leftovers = leftovers % makeNew
    return result
