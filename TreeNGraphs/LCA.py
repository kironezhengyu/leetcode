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
    3     5  7   9
'''


root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(2)
root.left.left=  TreeNode(3)
root.left.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)



def countMatch(root, num1,num2):
    if root ==None:
        return 0
    matches  = countMatch(root.left,num1,num2) + countMatch(root.right,num1,num2)
    if root.val == num1 or root.val == num2:
        return 1+matches
    else:
        return matches
def LCA(root,num1,num2):
    if root == None:
        return None
    if root.val == num1 or root.val == num2:
        return root
    #only care about left sub stree
    matches  = countMatch(root.left,num1,num2)
    # there is one on the right, current must be the LCA
    if matches ==1:
        return root
    # both on the left subtree
    elif matches == 2:
        return LCA(root.left,num1,num2)
    # both on the right
    elif matches ==0:
        return LCA(root.right,num1,num2)

print LCA(root,3,5)











