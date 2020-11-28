def makeArrayConsecutive2(statues):
    statues.sort()
    i = 0
    j = 1
    lastPos = len(statues)-1
    result = 0
    while (i <= lastPos - 1) and (j <= lastPos):
      if statues[j] - statues[i] > 1:
          result += (statues[j] - statues[i] - 1)
      i += 1
      j += 1

    return result
