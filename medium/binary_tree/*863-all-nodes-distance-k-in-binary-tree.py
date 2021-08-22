#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-07-28 00:11
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.parent_res = {}
        self.ans = []

    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """

        def findFatherNode(root):
            if not root:
                return
            if root.left:
                self.parent_res[root.left.val] = root
                findFatherNode(root.left)
            if root.right:
                self.parent_res[root.right.val] = root
                findFatherNode(root.right)

        def findNode(target, from_node, path, K):
            """

            :param target:
            :param from_node: from是避免回到当前节点，左右子树不会，但是根可能会
            :param path:
            :param K:
            :return:
            """
            if not target:
                return
            if path == K:
                self.ans.append(target.val)
                return
            if target.left != from_node:
                findNode(target.left, target, path + 1, K)
            if target.right != from_node:
                findNode(target.right, target, path + 1, K)
            if self.parent_res.get(target.val, None) != from_node:
                parent_node = self.parent_res.get(target.val, None)
                findNode(parent_node, target, path + 1, K)

        findFatherNode(root)
        findNode(target, None, 0, k)
        return self.ans

