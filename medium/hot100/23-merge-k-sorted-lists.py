# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 2:22 下午
# @Author  : Mohn
# @FileName: 23-merge-k-sorted-lists.py
"""
在two-sorted-list的基础上进行k个链表的合并。
两个链表的合并，一个长链表，从mid一分为二，然后左右合并。
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def merge2List(self, p1, p2):

        head = ListNode()
        tail = head

        while p1 and p2:
            if p1.val < p2.val:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next
        tail.next = p1 if p1 else p2
        return head.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        ## 分而治之
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        mid = n // 2
        return self.merge2List(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))


if __name__ == "__main__":
    s = Solution()
    l1 = None
    l2 = ListNode(-2)
    l3 = ListNode(-3)
    l3.next = ListNode(-2)
    l3.next.next = ListNode(1)
    L = s.mergeKLists([l1, l2, l3])
    while L:
        print(L.val)
        L = L.next
