#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-07-21 23:00
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def dfs(root):
            if not root:
                return 0
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            return max(left_depth, right_depth) + 1
        diff = abs(dfs(root.left)-dfs(root.right))
        return diff<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

