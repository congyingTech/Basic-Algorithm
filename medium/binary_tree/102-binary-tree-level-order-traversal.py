# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 12:22 上午
# @Author  : Mohn
# @FileName: test.py
"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal

时间复杂度是O(n),n个结点进出。
103题和102题基本一致，就是区分奇数层和偶数层即可

"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [root]
        res = []
        next_queue = []
        level_data = []
        while queue:
            r = queue.pop(0)
            level_data.append(r.val)
            if r.left:
                next_queue.append(r.left)
            if r.right:
                next_queue.append(r.right)
            if not queue:
                res.append(level_data)
                queue = next_queue[:]
                level_data = []
                next_queue = []
        return res


if __name__ == "__main__":
    #
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    s = Solution()
    print(s.levelOrder(root))
