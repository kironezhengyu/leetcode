'''
kth item in BST
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


#in-order treversal

def inOrder1(root,k):
    stack=[]
    result = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            result.append(root)
            root = root.right

    return result

    return result


def inOrder(root,k):
    if root==None or k<0:
        return -1
    inOrder(root.left,k)
    k-=1
    if k==0:
        return root, k
    inOrder(root.right,k)

print inOrder(root,1)









