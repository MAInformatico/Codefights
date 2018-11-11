import collections
def firstNotRepeatingCharacter(s):
    result = '_'
    lista = [s.index(i) for i,j in collections.Counter(s).items() if j==1]
    if lista != []:
        result = s[min(lista)]
    return result
