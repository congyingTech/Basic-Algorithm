# encoding:utf-8
"""
问题描述：对子树的结点中不含有1的结点进行剪枝
解决方法：递归的方法，递归判断左右子树是否含有1
"""
# Definition for a binary binary_tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def containsOne(node):
            if not node:
                return False
            node_left = node.left
            node_right = node.right
            a1 = containsOne(node_left)
            a2 = containsOne(node_right)
            if not a1:
                node.left = None
            if not a2:
                node.right = None
            return node.val == 1 or a1 or a2
        
        return root if containsOne(root) else None


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(0)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)
    root.left.left.left = TreeNode(0)

    s.pruneTree(root)

