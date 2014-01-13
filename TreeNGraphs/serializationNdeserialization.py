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
    _30_ 
   /    \    
  10    20
 /     /  \ 
50    45  35
'''

root = TreeNode(30)
root.left = TreeNode(10)
root.left.left=  TreeNode(50)


root.right = TreeNode(20)
root.right.right = TreeNode(35)
root.right.left = TreeNode(45)


# root = TreeNode('F')
# root.left = TreeNode('B')
# root.left.left=  TreeNode('A')
# root.left.right = TreeNode('D')
# root.left.right.left = TreeNode('C')
# root.left.right.right = TreeNode('E')

# root.right = TreeNode('G')
# root.right.right = TreeNode('I')
# root.right.right.left = TreeNode('H')

# root = TreeNode('A')
# root.right = TreeNode('B')
# root.right.right = TreeNode('C')
# root.right.right.right = TreeNode('D')


#pre order treversal 
def serialization(root):
    stack = []
    stack.append(root)
    result = []
    while len(stack)!=0:
        current = stack.pop()
        if not current:
            result.append('#')
        else:
            result.append(current.val)
            stack.append(current.right)
            stack.append(current.left)

    return result

print serialization(root)

#rebuid 
def deserialization(arr):
    stack = []
    for num in arr[1:]:
        temp = TreeNode(num)
        stack.append(temp)
    while stack:
        current = stack.pop()
        try:
            int(current.val)
            current.left = stack.pop()
            current.right = stack.pop()
        except:
            continue
    return root

tree = deserialization(serialization(root))

def levelOrder(root):
    Q = []
    Q.append(root)
    while Q:
        current = Q.pop(0)
        print current.val,
        if current.left:
            Q.append(current.left)
        if current.right:
            Q.append(current.right)
def inOrder(root):
    stack =  []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            print root.val,
            root = root.right

print inOrder(root)







