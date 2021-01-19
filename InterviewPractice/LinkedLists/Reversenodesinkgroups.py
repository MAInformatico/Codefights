# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def reverseNodesInKGroups(l, k):
    iterator1 = ListNode(None)
    iterator2 = iterator1
    while l is not None:
        swapping = None
        lBak = l
        for i in range(k):
            if l is not None:
                tmp = ListNode(l.value)
                tmp.next = swapping
                swapping = tmp
                l = l.next
            else:
                swapping = lBak
        iterator2.next = swapping
        
        while iterator2.next is not None:
            iterator2 = iterator2.next
            
    return iterator1.next        
