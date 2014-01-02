'''
partition a LL around x that all nodes 
greater than x after smaller than x
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

head = ListNode(1)
addAll(head,[2,1,3,4,1])

def partition(head,x):
    pivot = ListNode(x)
    root = ListNode(-1)
    r_l =root
    p_l = pivot

    current = head
    while current :
        next = current.next
        if current.val < x:
            r_l.next = current
            r_l = current
        else:
            p_l.next = current
            p_l = current
            p_l.next = None
        current =  next
    r_l.next  = pivot.next

    return root.next
print partition(head,3)


