def domainType(domains):
    dic = {'.com' : "commercial", '.org' : "organization", '.net' : "network", 'info': "information"}
    laux = []
    for i in range(len(domains)):
        aux = domains[i]
        aux = aux[-4:]        
        laux.append(dic.get(aux))    
    return laux
