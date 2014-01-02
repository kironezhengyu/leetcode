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

l2 = ListNode(7)
addAll(l2,[1])


def checkPanlindrome(l1):
    length =0
    l1_ref = l1
    while l1_ref :
        length+=1
        l1_ref =l1_ref.next
    stack = []
    fast = l1
    for i in range(length/2):
        stack.append(fast.val)
        fast= fast.next
    while fast:
        if fast.val != stack.pop():
            return False
        fast =fast.next

    return True
print checkPanlindrome(l1)
print checkPanlindrome(l2)




