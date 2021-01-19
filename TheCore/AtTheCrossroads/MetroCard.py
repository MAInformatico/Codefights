def metroCard(lastNumberOfDays):
    aux = [28,30,31]
    rest = [aux[2]]
    if lastNumberOfDays == 31: return aux
    else:
        return rest
