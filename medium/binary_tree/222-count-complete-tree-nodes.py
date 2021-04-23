# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 11:18 上午
# @Author  : Mohn
# @FileName: 222-count-complete-tree-nodes.py
"""
完全二叉树的叶子结点

"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    ans = 0

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_count = self.countNodes(root.left)
        right_count = self.countNodes(root.right)
        return left_count+right_count+1


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(4)
    print(s.countNodes(root))


