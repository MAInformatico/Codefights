def getPoints(answers, p):
    questionPoints = lambda i, answers: answers + i if answers == True else answers - p

    res = 0
    for i, ans in enumerate(answers):
        res += questionPoints(i, ans)
    return res
