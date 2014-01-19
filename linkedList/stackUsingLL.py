'''
Implementation of a stack using LL
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


class Stack(object):
    """ A stack using LL"""
    def __init__(self,arr):
        self.size = 0
        self.head = None
        self.tail = None
        if arr:
            for o in arr:
                self.push(o)
    def isEmpty(self):
        if self.size ==0:
            return True
        return False
    def getSize(self):
        return self.size
    def push(self,obj):
        if self.head == None:
            self.head = ListNode(obj)
            self.tail = self.head
            self.size += 1
        else:
            oldHead = self.head
            while self.head.next!=None:
                self.head = self.head.next
            self.head.next = ListNode(obj)
            self.tail = self.head.next
            self.head = oldHead
            self.size +=1
    def pop(self):
        """just delete the tail node"""
        if self.tail == None:
            raise Exception('poping from empty stack')
        oldHead = self.head
        val = self.tail.val
        for i in range (self.size-2):
            self.head = self.head.next
        self.tail = self.head
        self.head = oldHead
        self.size-=1
        return val
    def peek(self):
        return self.tail.val

    def __repr__(self):
        return self.head.__repr__()


s = Stack([1,2,3,4,5,6,7])

print s.peek()
print s.pop()

print s.getSize()
while not s.isEmpty():
    print s.pop()











