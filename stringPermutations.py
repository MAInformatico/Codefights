def stringPermutations(s):
    if len(s) <= 1:
        return [s]
    else:
        combinations = []
        for e in stringPermutations(s[:-1]):
            for i in range(len(e)+1):
                combinations.append(e[:i] + s[-1] + e[i:])
                
        comb = []
        for i in combinations:
            if i not in comb:
                comb.append(i)
        
        comb.sort()
        return comb
