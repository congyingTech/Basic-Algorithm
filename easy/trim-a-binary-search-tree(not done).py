# Definition for a binary binary_tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        左根右的遍历是
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        root_val = root.val
        

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    s = Solution()
    s.trimBST(root, L, R)
