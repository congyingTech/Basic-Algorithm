
class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value= value
def getDepth(root):
    if root == None:
        return 0
    leftDepth = getDepth(root.left)
    rightDepth = getDepth(root.right)
    if leftDepth > rightDepth:
        return leftDepth + 1
    elif rightDepth >= leftDepth:
        return rightDepth + 1





