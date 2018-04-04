def sumOfTwo(a, b, v):
    al=len(a)
    bl=len(b)
    i=0
    j=bl-1
    a=sorted(a)
    b=sorted(b)
    while i<al:
      while bl>0:
          if a[i]+b[j]<v:
             break
          if a[i]+b[j]==v:
            return 1
          j-=1
          if j<0:
            return 0
      if a[i]+b[j]>v:
        break
      i+=1
    return 0
