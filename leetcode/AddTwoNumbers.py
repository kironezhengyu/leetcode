'''
You are given two linked lists 
representing two non-negative numbers. 
The vals are stored in reverse order and
each of their nodes contain a single val. 
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
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
addAll(l1,[9,9,9])
l2 = ListNode(5)
addAll(l2,[9,2,9])
print l1,l2
def addTwoNumbers(l1,l2):
    carry = 0
    num1 = l1
    num2 = l2
    head = ListNode()
    refrenceHead = head
    while num1 and num2 :
        result = 0
        if carry!=0:
            result +=1
            carry=0
        result +=  num1.val +num2.val
        if result > 9:
            carry = 1
            result -=10
        resultNode =  ListNode(result)
        head.next =  resultNode
        num1 = num1.next
        num2 = num2.next
        head =head.next

    #left overs 
    if num1:
        result = 0
        if carry!=0:
            result+=1
        result+= num1.val
        if result > 9:
            carry = 1
            result -=10
        resultNode =  ListNode(result)
        head.next =  resultNode
        num1 = num1.next
        head =head.next

    if num2:
        result = 0
        if carry!=0:
            result+=1
        result+= num2.val
        if result > 9:
            carry = 1
            result -=10
        resultNode =  ListNode(result)
        head.next =  resultNode
        num2 = num2.next
        head =head.next

    if carry!=0:
        head.next = ListNode(1)
    return refrenceHead.next
print addTwoNumbers(l1,l2)

