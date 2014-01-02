
'''
find nth to last elemnt in one loop

two Ptr
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
addAll(head,[2,1,3,4,1,321,3,45,6,765,8,989])

def findNth(head,n):
    fast = head
    slow = head
    step = 0
    for distance in range(n):
        if fast ==None:
            return 'out of bound'
        else:
            fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    return slow.val

print findNth(head)


