def isPower(n):
    if n==1:  return True;    
    for base in range(2,(int)(math.sqrt(n))+1) :
        exp = 2
        p = (int)(math.pow(base, exp))
  
        while (p<=n and p>0) :
            if (p==n) :
                return True             
            exp += 1
            p = math.pow(base, exp)
                    
    return False
