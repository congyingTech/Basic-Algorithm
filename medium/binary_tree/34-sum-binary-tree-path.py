#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-05-01 23:24
"""

# Definition for a binary tree node.
"""
解题思路：
深度优先遍历，中序遍历
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """
        paths = []
        path = []

        def rec(root, target_rest):
            if not root:
                return
            # 根
            path.append(root.val)
            target_rest = target_rest-root.val
            if target_rest == 0 and not root.left and not root.right:
                paths.append(list(path))
            # 左
            rec(root.left, target_rest)
            # 右
            rec(root.right, target_rest)
            # 回溯
            path.pop()

        rec(root, sum)
        return paths


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    target = 22
    print(s.pathSum(root, target))
