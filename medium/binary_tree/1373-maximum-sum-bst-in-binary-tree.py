#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-07-23 22:53
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.res = float('-inf')

    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        lower = float('-inf')
        upper = float('inf')

        def isBST(root, lower, upper):
            if not root:
                return True
            val = root.val
            if val >= upper or val <= lower:
                return False
            if not isBST(root.left, lower, root.val):
                return False
            if not isBST(root.right, root.val, upper):
                return False
            return True

        def getPathSum(root):
            if not root:
                return 0
            cur_sum = root.val + getPathSum(root.left) + getPathSum(root.right)
            self.res = max(self.res, cur_sum)
            return cur_sum

        def dfs(root):
            if not root:
                return
            if isBST(root, lower, upper):
                # self.res = max(self.res, getPathSum(root))
                getPathSum(root)
                return
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return max(self.res, 0)
