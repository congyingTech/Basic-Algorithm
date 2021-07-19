# -*- coding: utf-8 -*-
# @Time    : 2021/7/19 11:43 上午
# @Author  : Mohn
# @FileName: 116-populating-next-right-pointers-in-each-node.py
"""
     1
   /  \
  2    3
 / \  / \
4  5  6  7
变成
     1
   /  \
  2 -> 3
 / \  / \
4->5->6->7


根左右的框架
"""

# Definition for a Node.

class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect_wrong(self, root):
        """
        :type root: Node
        :rtype: Node
        这种做法，导致跨父节点的两个子树无法相连

        """
        if not root or not root.left:
            return
        root.left.next = root.right
        self.connect(root.left)
        self.connect(root.right)
        return root

    def helper(self, node1, node2):
        if not node1 or not node2:
            return
        node1.next = node2
        self.helper(node1.left, node1.right)
        self.helper(node2.left, node2.right)
        self.helper(node1.right, node2.left)

    def connect(self, root):
        if not root:
            return
        self.helper(root.left, root.right)
