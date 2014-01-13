
class ListNode():
    val = 0
    next = None
    def __init__(self,x=0):
        self.val = x
        self.next = None
    def __repr__(self):
        toReturn = ''
        while(self.next!= None):
            toReturn+= 'I am '+str(self.val) +' My next is '+str(self.next.val)+'\n'
            self = self.next.next
        if(self!=None):
            toReturn += 'The last one is '+str(self.val)
        else:
            return toReturn
        return toReturn
        


def addAll(head,arr):
    refrenceHead = head
    for value in arr:
        temp = ListNode(value)
        head.next = temp
        head = temp
    return refrenceHead
'''
    _____
   |     |
1->2->3->4>
'''
head = ListNode(1)
addAll(head,[2,3,4])

head.next.next.next = head.next

head2 = ListNode(2)
addAll(head2,[3,4,5,6])


def solution(node):
    if node ==None:
        return False
    slow = node
    fast = node.next
    while True:
        if(slow == None or fast ==None):
            return False
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False

print solution(head)


