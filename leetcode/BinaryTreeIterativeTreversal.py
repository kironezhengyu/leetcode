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
        8      2
      /  \    /
    3     5  2
'''

root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(2)
root.left.left=  TreeNode(3)
root.left.right = TreeNode(5)
root.right.left = TreeNode(2)

def preOrder(root):
    
    #base case
    if root == None:
        return
    stack = []
    stack.append(root)

    '''
    Pop all items one by one. Do following for every popped item
       a) print it
       b) push its right child
       c) push its left child
    Note that right child is pushed first so that left is processed first
    '''
    res = []
    while len(stack)!=0:
        current = stack.pop()
        print current.val
        res.append(current.val)
        
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return res

#print preOrder(root)

def postOrder(root):
    if root == None:
        return
    stack = []
    output = []
    stack.append(root)
    while len(stack)!=0:
        current = stack.pop()
        output.append(current.val)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return output[::-1]
print postOrder(root)

def inOrder(root):
    #base case
    if root == None:
        return
    stack = []
    res =[]
    current =root
    while True:
        if current != None:
            stack.append(current)
            current = current.left
        else:
            if len(stack)!=0:
                current = stack.pop()
                res.append(current.val)
                current = current.right
            else:
                break
    return res
#print inOrder(root)






