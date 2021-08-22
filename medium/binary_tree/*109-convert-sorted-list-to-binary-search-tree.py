#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-07-25 23:41
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        def getMedian(left, right):
            p1 = left
            p2 = left
            while p1 != right and p1.next != right:
                p1 = p1.next.next
                p2 = p2.next
            return p2

        def buildBST(left, right):
            if left == right:
                return
            mid = getMedian(left, right)
            root = TreeNode(mid.val)
            root.left = buildBST(left, mid)
            root.right = buildBST(mid.next, right)
            return root

        return buildBST(head, None)
