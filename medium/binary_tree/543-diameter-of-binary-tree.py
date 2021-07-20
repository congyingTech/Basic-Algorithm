#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-07-20 01:02
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

"""

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def __init__(self):
        self.ans = 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def inner_dfs(root):
            if not root:
                return 0
            left_max_path = inner_dfs(root.left)
            right_max_path = inner_dfs(root.right)
            self.ans = max(self.ans, left_max_path + right_max_path + 1)

            return max(left_max_path, right_max_path) + 1

        inner_dfs(root)
        return self.ans - 1