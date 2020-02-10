# encoding:utf-8
"""
问题描述：
输入两个链表，找出它们的第一个公共结点。
解决方案：
有公共结点的链表的特点是：遇到第一个公共结点之后，所有的结点就都是重合的了，不可能再出现分叉。
首先遍历出两个两边的长度，较长的那个先走差值步，然后两个链表一起遍历，直到遇见相同的公共结点。
"""

class LinkedNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def findFirstCommonNode(self, l1, l2):
        n1, n2 = 0, 0
        h1, h2 = l1, l2
        while h1:
            n1 += 1
            h1 = h1.next
        while h2:
            n2 += 1
            h2 = h2.next
        print(n1,n2)
        p1, p2 = l1, l2

        if n1 > n2:
            delta = n1-n2
            while delta>0:
                p1 = p1.next
                delta -= 1 
        else:
            delta = n2-n1
            while delta>0:
                p2 = p2.next
                delta -= 1
        while p1!=p2:
            p1 = p1.next
            p2 = p2.next
        print(p1.val)
        return p1

if __name__ == "__main__":
    s = Solution()
    common_node = LinkedNode(3)
    l1 = LinkedNode(1)
    l1.next = LinkedNode(2)
    l1.next.next = common_node
    common_node.next = LinkedNode(4)
    common_node.next.next = LinkedNode(11) 

    l2 = LinkedNode(9)
    l2.next = common_node
   
    

    s.findFirstCommonNode(l1, l2)