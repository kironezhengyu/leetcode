'''
A stack that can rewturn minimum so far
'''

class MinStack(object):
    stack = []
    currentMin = 0
    def __init__(self,arr=None):
        if arr != None:
            for obj in arr:
                self.push(obj)

    def push(self,obj):
        self.stack.append(obj)
        if obj < self.currentMin:
            self.currentMin = obj
    def pop(self):
        return self.stack.pop()
    def popMin(self):
        return self.currentMin


s  =  MinStack([1,2,2,3,4,5,1,-1,2,3,4,5])
print s.popMin()
print s.pop()