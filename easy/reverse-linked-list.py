# encoding:utf-8
"""
问题描述：反转链表
解决方案：三个指针解决，pre，cur，next_node
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        pre = head
        cur = pre.next
        pre.next = None
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre
    
    def printLinkList(self, head):
        while head:
            print(head.val)
            head = head.next

if __name__ == "__main__":
    s = Solution()
    head = ListNode(3)
    head.next = ListNode(4)
    head.next.next = ListNode(5)
    head.next.next.next = ListNode(6)
    head.next.next.next.next = ListNode(7)
    pre = s.reverseList(head)
    s.printLinkList(pre)