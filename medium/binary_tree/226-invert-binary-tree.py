# -*- coding: utf-8 -*-
# @Time    : 2021/7/19 11:26 上午
# @Author  : Mohn
# @FileName: 226-invert-binary-tree.py

# Definition for a binary tree node.
"""
二叉树的反转=镜像二叉树

根左右框架
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    s.invertTree(root)
