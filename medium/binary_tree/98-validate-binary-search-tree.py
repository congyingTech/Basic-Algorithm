# -*- coding: utf-8 -*-
# @Time    : 2021/5/6 5:22 下午
# @Author  : Mohn
# @FileName: 98-validate-binary-search-tree.py
"""

根左右的框架
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        lower = float('-inf')
        upper = float('inf')

        def helper(root, lower, upper):
            if not root:
                return True

            val = root.val
            if val <= lower or val >= upper:
                return False
            if not helper(root.left, lower, val):
                return False
            if not helper(root.right, val, upper):
                return False
            return True
        return helper(root, lower, upper)


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    print(s.isValidBST(root))
