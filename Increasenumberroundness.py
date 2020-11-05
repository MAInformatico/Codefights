def increaseNumberRoundness(n):    
    while n%10==0:
        n //= 10    
    check = 1
    while n:
        check *= n%10
        n//=10    
    if check ==0: return True
    else:
        return False      
