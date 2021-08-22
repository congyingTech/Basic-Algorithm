#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-10 00:10
"""


class Solution(object):
    def __init__(self):
        self.x_parent = None
        self.x_depth = 0
        self.x_found = False
        self.y_parent = None
        self.y_depth = 0
        self.y_found = False

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """

        def dfs(root, depth, parent):
            if not root:
                return
            if root.val == x:
                self.x_parent = parent
                self.x_depth = depth
                self.x_found = True
            if root.val == y:
                self.y_parent = parent
                self.y_depth = depth
                self.x_found = True
            if self.x_found and self.y_found:
                return
            dfs(root.left, depth + 1, root)
            if self.x_found and self.y_found:
                return
            dfs(root.right, depth + 1, root)

        dfs(root, 0, None)
        return self.x_parent != self.y_parent and self.x_depth == self.y_depth