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

#print serialization(root)
arr = [30, 10, 50, '#', '#', '#', 20, 45, '#', '#', 35, '#', '#']
#rebuid 

index = 0
def deserialization(arr,node):
    if index >= len(arr):
        return
    if arr[index]=='#':
        index +=1
        return
    current = arr[index]
    node = TreeNode(current)
    index+=1
    node.left = deserialization(arr,node.left)
    node.right = deserialization(arr,node.right)
    return node




Tree = deserialization(arr,None)

def preorder(tree):
    if tree==None:
        return
    print tree,
    preorder(tree.left)
    preorder(tree.right)

print preorder(Tree)
#tree = deserialization(serialization(root))

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

#print levelOrder(Tree)


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

#print inOrder(root)







