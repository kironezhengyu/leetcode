from collections import deque
class Q(object):
    def __init__(self,arr=None):
        self.inStack = []
        self.outStack = []
        if arr is not None:
            for v in arr:
                self.enqueue(v)
    def enqueue(self,v):
        self.inStack.append(v)
        
    def dequeue(self):
        while len(self.inStack) >0 :
            self.outStack.append(self.inStack.pop())
        return self.outStack.pop()
    def __len__(self):
        return len(self.inStack)


q =  Q([1,2,3,4])
print q.dequeue()



class Stack(object):
    def __init__(self,arr=None):
        self.inQueue = deque()
        self.outQueue = deque()
        if arr is not None:
            for v in arr:
                self.push(v)
    def push(self,v):
        self.inQueue.append(v)
        
    def pop(self):
        while len(self.inQueue) > 0:
            self.outQueue.append(self.inQueue.popleft())
        return self.outQueue.popleft()

s =  Stack([1,2,3,4])
print s.pop()