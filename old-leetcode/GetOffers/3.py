#输入一个链表，从尾到头打印链表每个节点的值。

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        head = listNode
        value = []
        while(head):
            value.insert(0,head.val)
            head = head.next
        return value
if __name__ == '__main__':
    s = Solution()
    listNode = ListNode(1)
    listNode.next = ListNode(2)
    listNode.next.next = ListNode(3)
    str = s.printListFromTailToHead(listNode)
    print(str)