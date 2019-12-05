# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    rootval = 0
    #右根左遍历，rootval记录总和
    def convertBST(self, root):
        #下面的这种做法理解错了，题意是每个节点上的值变为比他大的值的和
        if root == None:
            return 
        if root.right:
            self.convertBST(root.right)
        root.val += self.rootval
        self.rootval = root.val
        if root.left:
            self.convertBST(root.left)
        return root
    
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    root.left = TreeNode(0)
    root.right = TreeNode(3)
    root.left.left = TreeNode(-4)
    root.left.right = TreeNode(1)
    s.convertBST(root)
    print(s.bianli(root))
        
