
'''


You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''


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
head = ListNode(1)
addAll(head,[2,3,4])


def reverseHalf(node):
    output = []
    while node!=None:
        output.append(node)
        node = node.next
    return output

def solution(node):
    if node ==None:
        return
    stack = reverseHalf(node)
    length = len(stack)
    if length == 1:
        return node
    refrenceHead = node
    mid = length/2
    current = node
    next = node.next
    
    while mid >=0 :
        insert = stack.pop()
        insert.next = next
        current.next = insert
        current = next
        next = next.next
        mid-=1
    next.next = None

    return refrenceHead

print solution(head)










