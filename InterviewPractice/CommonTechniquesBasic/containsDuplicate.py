def containsDuplicates(a):
    b = set(a)
    mynewlist = list(b)
    if len(mynewlist) == len(a):
        return False    
    else:
        return True
