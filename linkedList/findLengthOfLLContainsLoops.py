
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
 ________
|        |
1->2->3->4>
'''
head = ListNode(1)
addAll(head,[2,3,4])

head.next.next.next = head

def sol1(head):
    counter =2
    if head:
        temp =  head.next
        while temp!=head:
            counter+=1
            temp = temp.next
    return counter
print sol1(head)





def permutation1(string):
    result = []
    for s in string:
        for i in range(len(string)):
            result.append((string[i:]+s+string[:i]))
    return result

def perms(word):
    stack = list(word)
    results = [stack.pop()]
    while len(stack) != 0:
        c = stack.pop()
        new_results = []
        for w in results:
            for i in range(len(w)+1):
                new_results.append(w[:i] + c + w[i:])
        results = new_results
    return results

#print perms('abcdsada')





