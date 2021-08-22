#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-07-26 21:36
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        p1 = ListNode(-1)
        p1.next = head
        p2 = ListNode(-1)
        p2.next = head

        while left > 1:
            p1 = p1.next
            left -= 1
        while right:
            p2 = p2.next
            right -= 1

        tail_node = p2.next

        def reverse(head):
            p1 = None
            p2 = head
            while p2:
                p3 = p2.next
                p2.next = p1
                p1 = p2
                p2 = p3
            return p1

        node_between = p1.next
        p_between = node_between
        while p_between!=p2:
            p_between = p_between.next
        p_between.next = None

        head_reversed = reverse(node_between)
        p1.next = head_reversed

        while p1.next:
            p1 = p1.next
        p1.next = tail_node

        p = head
        while p:
            print(p.val)
            p = p.next
        return head


class Solution1(object):
    def reverseBetween(self, head, left, right):

        def reverse(head):
            p1 = None
            p2 = head
            while p2:
                p3 = p2.next
                p2.next = p1
                p1 = p2
                p2 = p3

        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node  # pre是前置节点
        # 第一步：走left-1步，找到需要反转部分的前置节点
        gap = left-1
        while gap:
            pre = pre.next
            gap -= 1
        left_p = pre.next

        # 第二步：从pre前置节点，向后走right-left+1步
        right_p = pre
        gap = right-left+1
        while gap:
            right_p = right_p.next
            gap -= 1
        succ = right_p.next  # 保存后置节点

        # 第三步：切断需要反转的链表
        pre.next = None
        right_p.next = None

        # 第四步：反转操作
        reverse(left_p)

        # 第五步：连接操作
        pre.next = right_p
        left_p.next = succ

        return dummy_node.next











if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)

    s.reverseBetween(head, 1, 2)
