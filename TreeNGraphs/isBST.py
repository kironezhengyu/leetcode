class TreeNode():
    val = 0
    left = None
    right = None
    def __init__(self,x=0):
        self.val = x
    def __repr__(self):
        return ' ' + str(self.val)

'''
Construct a Tree
            10
          /   \
        8     11
      /  \    / \
    3     9  7   12
'''


root = TreeNode('F')
root.left = TreeNode('B')
root.left.left=  TreeNode('A')
root.left.right = TreeNode('D')
root.left.right.left = TreeNode('C')
root.left.right.right = TreeNode('E')

root.right = TreeNode('G')
root.right.right = TreeNode('I')
root.right.right.left = TreeNode('H')

root1 =  TreeNode(5)
root1.left = TreeNode(4)
root1.right = TreeNode(3)

def isBST(root):
    if root.left!=None:
        if root.val > root.right.val or isBST(root.left)==False :
            return False
    if root.right!=None:
        if root.val < root.left.val or isBST(root.right)==False :
            return False
    return True


previous = 0
#in-order print
def isBST2(root):
    if root.left:
        isBST2(root.left)
    if root!=None:
        if root.val < previous:
            result.append(-999)
        else:
            result.append(root)
    if root.right:
        isBST2(root.right)

#pre-order iterative:
def isBST5(root):
    stack = []
    stack.append(root)
    result =[]
    while len(stack)!=0:
        current = stack.pop()
        result.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
        
    return result[::]

#in-order
#so smart...
def isBST6(root):
    stack = []
    result = []
    while len(stack)!=0 or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            result.append(root)
            root = root.right

    return result

def isBST3(root):
    #dfs ---post order-
    stack = []
    stack.append(root)
    result =[]
    while len(stack)!=0:
        current = stack.pop()
        result.append(current.val)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
        
    return result[::-1]


def isBST4(root):
    #bfs ---level order
    stack = []
    stack.append(root)
    result =[]
    while len(stack)!=0:
        current = stack.pop(0)
        result.append(current.val)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

        
    return result[:]

def allSubSet(arr):
    result = [[]]
    current = []
    for num in arr:
        current = []
        for lists in result:
            current.append(lists+[num])
        result+=current
        #result += [ x+[num] for x in result]
    return result
#print allSubSet([1,2,3,4])

#print allSubSet('abcdsada')

'''
    15
    /\
    2  2
   /   \ 
  3     3


'''



root2= TreeNode(15)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.left = TreeNode(3)
root2.right.right = TreeNode(3)

def isMirror(root):
    return isMirrorHelper(root.left,root.right)

def isMirrorHelper(left,right):
    print left,right
    return left==right==None
    return left.val==right.val and isMirrorHelper(left.left,right.right) and isMirrorHelper(left.right,right.left)
print isBST4(root2)

print isMirror(root2)





print isBST6(root)
#print result[:]


