#二叉树的深度遍历
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        
        return leftDepth+1 if leftDepth > rightDepth else rightDepth+1   
        

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.right = TreeNode(4)
    root.left.right.right = TreeNode(3)
    print(Solution().maxDepth(root))