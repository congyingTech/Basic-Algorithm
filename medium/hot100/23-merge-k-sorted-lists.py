# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 2:22 下午
# @Author  : Mohn
# @FileName: 23-merge-k-sorted-lists.py
"""
在two-sorted-list的基础上进行k个链表的合并。
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge2List(list1, list2):
            head = ListNode(-1)
            tail = head
            p1 = list1
            p2 = list2
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
        L = ListNode(-1)
        for l in lists:
            L = merge2List(L, l)
        return L.next


if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l2 = ListNode(2)
    l2.next = ListNode(3)
    l2.next.next = ListNode(5)
    l1.next.next = ListNode(6)
    l3 = ListNode(1)
    l3.next = ListNode(5)
    l3.next = ListNode(8)
    L = s.mergeKLists([l1, l2, l3])
    while L:
        print(L.val)
        L = L.next
