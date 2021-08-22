#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-21 23:42
"""


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.sort_list(head, None)

    def sort_list(self, head, tail):
        if not head:
            return head
        if head.next == tail:
            head.next = None
            return head
        # step1:快慢指针寻找mid的过程
        slow = fast = head
        while fast != tail:
            fast = fast.next
            slow = slow.next
            if fast != tail:
                fast = fast.next
        mid = slow
        # step2:合并两个排序好的链表
        return self.mergeTWoList(self.sort_list(head, mid), self.sort_list(mid, tail))

    def mergeTWoList(self, l1, l2):

        if l1.val < l2.val:
            p1 = l1
            p2 = l2
        else:
            p2 = l1
            p1 = l2
        res = p1
        while p2:
            if not p1.next:
                p1.next = p2
                break
            p1_next = p1.next
            p2_next = p2.next
            if p2.val <= p1_next.val:
                p1.next = p2
                p2.next = p1_next
                p2 = p2_next
            else:
                p1 = p1.next
        return res
