def additionWithoutCarrying(param1, param2):
    result = 0  
    multiplier = 1
    bit_sum = 0
  
    while (param1 or param2) : 
        bit_sum = ((param1 % 10) + (param2 % 10))            
        bit_sum = bit_sum % 10          
        result = (bit_sum * multiplier) + result 
        param1 = math.floor(param1 / 10) 
        param2 = math.floor(param2 / 10)           
        multiplier = multiplier * 10
      
    return result 
