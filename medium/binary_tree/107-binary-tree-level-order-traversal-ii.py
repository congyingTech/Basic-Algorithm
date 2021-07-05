#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-05-01 23:08
解题思路：
层序遍历+reverse

"""
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        queue = [root]
        level_val = []
        next_queue = []
        while queue:
            node = queue.pop(0)
            level_val.append(node.val)
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
            if not queue:
                queue = next_queue
                ans.append(level_val)
                level_val = []
                next_queue = []
        return ans[::-1]


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(s.levelOrderBottom(root))
