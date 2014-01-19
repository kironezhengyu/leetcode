'''
get depth of tree both recursion and iterative
'''

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


def getDepthRecursion(tree):
    if tree ==None:
        return 0
    return 1 + max(getDepthRecursion(tree.left), getDepthRecursion(tree.right))

print getDepthRecursion(root)

def getDepthInterative(tree):
    Q = []
    Q.append(tree)
    special = TreeNode('#')
    Q.append(special)
    depth = 0
    treversal = []
    while Q:
        current = Q.pop(0)
        treversal.append(current)
        if current==special and len(Q)!=0:
            print Q
            depth+=1
            Q.append(special)

        if current.left:
            Q.append(current.left)
        if current.right:
            Q.append(current.right)

    print treversal
    return depth

print getDepthInterative(root)







