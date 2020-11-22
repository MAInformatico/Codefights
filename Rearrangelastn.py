# Singly-linked lists are already defined with this interface:
 class ListNode(object):
   def __init__(self, x):
     self.value = x
     self.next = None

def rearrangeLastN(l, n):    
    if not l or n==0:
        return l
    iterator = cur = l
    lenght=1
    while iterator.next is not None:
        lenght +=1
        iterator = iterator.next
    if lenght==n:
        return l
    stp=lenght-n-1
    for s in range(stp):
        cur=cur.next
    iterator.next,cur.next,l=l,None,cur.next
    return l            
