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
            5
          /   \
        4      7
      /  \    /
    3     6  4
'''

root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(2)
root.left.left=  TreeNode(3)
root.left.right = TreeNode(5)
root.right.left = TreeNode(2)


root1 =  TreeNode(5)
root1.left = TreeNode(4)
root1.right = TreeNode(7)

def isBST(root):
    if root.left!=None:
        if root.val > root.right.val or isBST(root.left)==False :
            return False
    if root.right!=None:
        if root.val < root.left.val or isBST(root.right)==False :
            return False
    return True

print isBST(root1)
print isBST(root)


