'''
implement a series of stack that has multiple stacks
'''

class SetOfStack(object):
    def __init__(self,values=None,maxlen=2):
        self.maxlen = maxlen
        self.stacks  =[[]]
        if values is not None:
            for v in values:
                self.push(v)
    def push(self,value):
        if len(self.stacks[-1]) >= self.maxlen:
            self.stacks.append([])
        self.stacks[-1].append(value)
    def pop(self):
            if len(self.stacks) == 1 and not self.stacks[0]:
                raise IndexError('pop from empty stack')
            if not self.stacks[-1]:
                self.stacks.pop()
            return self.stacks[-1].pop()
    def popAt(self,x=-1):
        print self.stacks
        return self.stacks[x].pop()

s  = SetOfStack([1,1,1,2,3,4,5,1,3,45,5,43])
print s.pop()
print s.popAt(5)


