import random
'''
Sort a linked list in O(n log n) time 
using constant space complexity.
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
head = ListNode(3)
addAll(head,[1,2,4,6])
#addAll(head,random.sample(range(40),9))


def swap(n1,n2):
    # n1--->n2
    # n2--->n3
    temp  = n2.next
    n2.next = n1
    n1.next = temp
    


def selectionSort(head):
    if head is None:
        return None
    refHead = head
    next = head.next
    while(next!=None):
        if next.val < head.val:
            swap(head,next)
        head = head.next
        next = next.next
    return refHead



def sortLinkedListInsertionSort(node):
    prev = node
    ptr1 = node.next
    
    
    while ptr1:
        ptr2 = node
        prev2 = None
        while ptr2.val < ptr1.val and ptr1 != ptr2:
            prev2 = ptr2
            ptr2 = ptr2.next
            
        if ptr2 == ptr1:
            prev = prev.next
            ptr1 = ptr1.next
            continue
        
        if ptr2 == node:
            # at the beginning
            prev.next = ptr1.next
            ptr1.next = node
            node = ptr1
            
        else:
            prev.next = ptr1.next
            prev2.next = ptr1
            ptr1.next = ptr2
            
        ptr1 = prev.next
        

    return node
    
print sortLinkedListInsertionSort(head)





    