'''
1-2-3-4-5-6
-1-2-3-4-5-9--10
'''

class ListNode():
    val = 0
    next = None
    def __init__(self,x=0):
        self.val = x
        self.next = None
    def __repr__(self):
        if self.next:
            return '%d--->%s' % (self.val, str(self.next))
        else:
            return '%d' % (self.val)
        


def addAll(head,arr):
    refrenceHead = head
    for value in arr:
        temp = ListNode(value)
        head.next = temp
        head = temp
    return refrenceHead
l1 = ListNode(1)
addAll(l1,[9,8,11,10])
l2 = ListNode(3)
addAll(l2,[1,23,4,6,8])


def solution(l1,l2):
    
