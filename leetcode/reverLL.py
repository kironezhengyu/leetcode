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
addAll(head,[2,3,4])

def reverse(head):

    previous = None
    #swap pointer
    
    while head:
        next = head.next
        head.next =previous
        previous =head
        head = next
    return previous
print reverse(head)



