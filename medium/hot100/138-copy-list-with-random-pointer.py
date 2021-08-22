#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-07-22 22:59
"""
# Definition for a Node.



# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return
        pre = head
        # 1)主链表上节点的复制
        while pre:
            copy_node = Node(pre.val)
            next_node = pre.next
            pre.next = copy_node
            copy_node.next = next_node
            pre = next_node
        # 2)random节点指向复制
        pre = head
        while pre:
            if pre.random:
                pre.next.random = pre.random.next
            pre = pre.next.next
        # 3)原链表与复制链表的拆离
        p1 = head
        dummy = Node(-1,None,None)
        p2 = dummy
        while p1:
            p2.next = p1.next
            p2 = p2.next
            p1.next = p2.next
            p1 = p1.next


        return dummy.next


if __name__ == "__main__":
    s = Solution()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    node1.random = node3
    node2.random = node4

    res = s.copyRandomList(node1)
