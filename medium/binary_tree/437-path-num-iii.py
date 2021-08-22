#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-08 16:19

对于遍历到的当前节点，路径数=当前节点和为target的路径数+左子树和为target的路径数+右子树中和为target的路径数

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def __init__(self):
        self.count = 0

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        if not root:
            return 0
        self.dfs(root, targetSum)
        self.pathSum(root.left, targetSum)
        self.pathSum(root.right, targetSum)
        return self.count

    def dfs(self, root, targetSum):
        if not root:
            return
        if targetSum-root.val == 0:
            self.count += 1
        self.dfs(root.left, targetSum-root.val)
        self.dfs(root.right, targetSum-root.val)


if __name__ == "__main__":
    s = Solution()


