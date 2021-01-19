def countSumOfTwoRepresentations2(n, l, r):
  auxlist=[]
  result=0
  for i in range(l,r+1):
    auxlist.append(i)
  for i in reversed(auxlist):
    for j in reversed(auxlist):
      if i+j == n: result+=1
    del(auxlist[-1])
  return result
