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

middle = head.next.next.next


def deleteMiddle(middle):
    
    next = middle.next
    middle.val = next.val
    middle.next = next.next

print head
print deleteMiddle(middle)
print head


