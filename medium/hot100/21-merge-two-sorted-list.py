# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 7:27 下午
# @Author  : Mohn
# @FileName: 21-merge-two-sorted-list.py

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        # 空间复杂度为O(1)
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 is not None else l2

        return prehead.next


if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l2 = ListNode(2)
    l2.next = ListNode(3)
    l2.next.next = ListNode(5)
    l1.next.next = ListNode(6)
    l = s.mergeTwoLists(l1, l2)
    while l:
        print(l.val)
        l=l.next

