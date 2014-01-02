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
    def isEmpty(self):
        return (len(self.inStack) + len(self.outStack)) ==0

class TreeNode():
    val = 0
    left = None
    right = None
    def __init__(self,x=0):
        self.val = x
    def __repr__(self):
        return ' ' + str(self.val)

def isBST(root):
    if root.left!=None:
        if root.val < root.left.val or isBST(root.left)==False :
            return False
    if root.right!=None:
        if root.val >= root.right.val or isBST(root.right)==False :
            return False
    return True

def buildBST(arr,start,end):
    if end <start:
        return None
    mid = (start +end) / 2
    currentRoot = TreeNode(arr[mid])
    currentRoot.left = buildBST(arr,start,mid-1)
    currentRoot.right = buildBST(arr,mid+1,end)
    return currentRoot

def minimalHeight(arr):
    return buildBST(arr,0,len(arr)-1)

#gives level order treversal 
def bfs(root):
    q = deque()
    q.append(root)
    special = TreeNode(-1111)
    q.append(special)
    while len(q)>0:
        current = q.popleft()
        if current !=special:
            print current.val,
        if current == special and len(q)>0:
            q.append(special) #mark new level
            print
        if current.left: 
            q.append(current.left)
        if current.right: 
            q.append(current.right)  
#gives reversed pre-order treversal
def dfs(root):
    seen = set()
    stack = []
    stack.append(root)
    while len(stack)!=0:
        current = stack.pop()
        print current.val,
        if current.left: 
            stack.append(current.left)
        if current.right: 
            stack.append(current.right)
    print 
#flip between levels
def printLevel(root):
    thisLevel =[root]
    while thisLevel:
        nextLevel = []
        for n in thisLevel:
            print n.val,
            if n.left :nextLevel.append(n.left)
            if n.right: nextLevel.append(n.right)
        print
        thisLevel = nextLevel



root =  minimalHeight([1,2,3,4,5,6,7])

printLevel(root)
dfs(root)
bfs(root)
print isBST(minimalHeight([1,2,3,4,5,6,7]))


