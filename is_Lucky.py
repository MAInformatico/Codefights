def isLucky(n):
    nstring= str(n)
    length= len(nstring)
    cacho= nstring[0:length/2]
    mitad= nstring[length/2:length]
    
    return sum(cacho) == sum(mitad)
    
    
def sum(nstring):
    result=0
    for digit in nstring:
        result += int(digit)
    return result
