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
      /  \    / \
    3     5  2   2
'''


root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(2)
root.left.left=  TreeNode(3)
root.left.right = TreeNode(5)
root.right.left = TreeNode(2)




def getHeight(root):
    if root == None:
        return 0
    heightLeft =  getHeight(root.left)
    heightRight = getHeight(root.right)
    if heightRight <0 or heightRight<0 or abs(heightRight - heightLeft) > 1 :
        return -1
    else: 
        return max(heightRight,heightLeft)+1

def isBalanced(root):
    return getHeight(root) >=0


print isBalanced(root)