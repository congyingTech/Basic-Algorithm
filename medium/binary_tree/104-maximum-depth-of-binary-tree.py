# -*- coding: utf-8 -*-
# @Time    : 2021/4/29 10:40 上午
# @Author  : Mohn
# @FileName: 104-maximum-depth-of-binary-tree.py
"""
求二叉树的最大的深度
"""


class TreeNode(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(s.maxDepth(root))
