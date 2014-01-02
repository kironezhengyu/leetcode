from collections import deque
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
root =  minimalHeight([1,2,3,4,5,6,7])

levels = {}
def levelLinkedListDFS(root,depth):
    if root ==None:
        return
    levelLinkedListDFS(root.left,depth+1)
    levelLinkedListDFS(root.right,depth+1)
    try:
        levels[depth].append(root.val)
    except:
        levels[depth] = [root.val]
    return levels

print levelLinkedListDFS(root,0)

def levelLinkedListBFS(root):
    levels = {}
    q = deque()
    q.append(root)
    special = TreeNode(-1111)
    q.append(special)
    depth = 0
    while len(q)>0:
        current = q.popleft()
        if current !=special:
            try:
                levels[depth].append(current.val)
            except:
                levels[depth] = [current.val]
        if current == special and len(q)>0:
            q.append(special) #mark new level
            depth+=1
        if current.left: 
            q.append(current.left)
        if current.right: 
            q.append(current.right) 
    return levels 
print levelLinkedListBFS(root)


