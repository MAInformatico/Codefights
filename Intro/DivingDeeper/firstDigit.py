def firstDigit(inputString):
    for i in range(len(inputString)):
        if inputString[i].isdigit() == True:
            return inputString[i]
