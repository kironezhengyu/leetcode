'''
delete LL nodes with same value
'''

'''
Check to see if a LL is a pandlindrome or not
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
l1 = ListNode(7)
addAll(l1,[9,8,8,9,7])


def delteNode(head):
    pass