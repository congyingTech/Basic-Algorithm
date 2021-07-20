#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-07-20 01:39


给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：

例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
计算从根节点到叶节点生成的 所有数字之和 。

叶节点 是指没有子节点的节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

    def preOrderTraversal(self, root):
        stack = [root]
        stack_val = [root.val]
        res = []
        final = []
        while stack:
            cur = stack.pop()
            stack_val.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
                stack_val.append(cur.right.val)
            if cur.left:
                stack.append(cur.left)
                stack_val.append(cur.left.val)

            if not cur.left and not cur.right:
                final.append(res[:])
                res.pop()
            if not cur.left or not cur.

        print(final)

        return res


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.left.right.left = TreeNode(6)
    root.left.right.left.right = TreeNode(2)

    print(Solution().preOrderTraversal(root))