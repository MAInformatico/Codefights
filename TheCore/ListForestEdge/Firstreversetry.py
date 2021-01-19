def firstReverseTry(arr):
     return [arr[len(arr)-i-1] if (i==0)or(i==len(arr)-1) else arr[i] for i in range(0,len(arr))] 
