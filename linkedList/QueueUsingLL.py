'''
Implementation of Queue using LL
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

class Queue(object):
    """Doc String is awesome"""
    def __init__(self,arr):
        self.head =None
        self.tail = None
        self.size =0
        if arr:
            for o in arr:
                self.enqueue(o)
    def isEmpty(self):
        if self.size==0:
            return True
        return False
    def getSize(self):
        return self.size
    def enqueue(self,obj):
        """Acting like a queue FIFO"""
        if self.head ==None:
            self.head = ListNode(obj)
            self.tail = self.head
            self.size+=1
        else:
            self.tail.next = ListNode(obj)
            self.tail = self.tail.next
            self.size +=1
    def dequeue(self):
        if self.isEmpty():
            raise Exception('Q is empty')
        newHead = self.head.next
        val = self.head.val
        self.head = newHead
        self.size -=1
        return val

    def __repr__(self):
        return self.head.__repr__()


Q = Queue([1,2])

print Q
while not Q.isEmpty():
    print Q.dequeue()












