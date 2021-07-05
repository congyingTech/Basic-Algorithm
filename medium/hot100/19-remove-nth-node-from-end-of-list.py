# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 3:23 下午
# @Author  : Mohn
# @FileName: 19-remove-nth-node-from-end-of-list.py
"""
删除链表的倒数第N个结点
双指针的方法：其中一个指针先向前移动n步
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        p1 = head
        p2 = head

        while p1:

            while n:
                p1 = p1.next
                n -= 1
            if p1 and p1.next:
                p1 = p1.next
                p2 = p2.next
            elif p1 and p2.next:
                next_p = p2.next.next
                p2.next = next_p
                break
            elif not p1 and p2.next:
                p2 = p2.next
                return p2
            else:
                return None
        return head


if __name__ == "__main__":
    s = Solution()
    n = 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    new_head = s.removeNthFromEnd(head, n)
    while new_head:
        print(new_head.val)
        new_head = new_head.next