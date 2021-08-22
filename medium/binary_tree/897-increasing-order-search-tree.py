#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-07-21 23:51
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        new_tree = TreeNode(res[0])
        index = 1
        p1 = new_tree
        while index < len(res):
            p1.right = TreeNode(res[index])
            index += 1
            p1 = p1.right

        return new_tree