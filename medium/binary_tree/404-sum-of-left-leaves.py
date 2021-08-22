#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-07-26 01:33
"""


class Solution(object):
    def __init__(self):
        self.res = 0
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root and not root.left and not root.right:
            return 0
        def dfs(root, pos):
            if not root:
                return 0
            if not root.left and not root.right and pos%2==0:
                self.res+=root.val
            dfs(root.left, 2*pos)
            dfs(root.right, 2*pos+1)
        dfs(root, 0)

        return self.res