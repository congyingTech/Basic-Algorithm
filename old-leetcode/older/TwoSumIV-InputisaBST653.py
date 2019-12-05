# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        res = []#res存放中序遍历结果
        def getAllElem(root):
            if root == None:
                return 
            if root.left:
                getAllElem(root.left)
            res.append(root.val)
            if root.right:
                getAllElem(root.right)
            return res
        getAllElem(root)
        
        for i,e in enumerate(res):
            if (k - e) in res[0:i]+res[i+1:]:
                return True
        return False

#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
if __name__ == "__main__":
    s = Solution()
#     root = TreeNode(5)
#     root.left = TreeNode(3)
#     root.right = TreeNode(6)
#     root.left.left = TreeNode(2)
#     root.left.right = TreeNode(4)
#     root.right.right = TreeNode(7)
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(4)
    root.left.left = TreeNode(-2)
    root.right.left = TreeNode(3)
    
    k = 7
    
    print(s.findTarget(root, k))