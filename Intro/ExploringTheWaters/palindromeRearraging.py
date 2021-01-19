def count_letters(s,clean_null=False):
    r=dict(zip(map(chr,range(0,256)), [0]*255))
    for c in s:
        r[c]+=1
    if clean_null:
        r = dict([(k,i) for k,i in r.items() if i>0])
    return r

def palindromeRearranging(inputString):
    norep = count_letters(inputString,False)
    even =0
    noteven = 0
    for i in norep:
            if norep[i]%2 !=0:
                even+=1
            if norep[i]%2 ==0:
                noteven +=1
                
    if even ==1 or even==0 and noteven>1:
        return True
    else :
        return False
