# encoding:utf-8
"""
问题描述：
一个链表里面存在环，如何找出环的入口结点？
解决方案：
可用双指针的思路，定义两个指针p1，p2，指向链表的头结点，
如果链表中的环有n个结点，那么p1先在链表上移动n步，然后两个结点以相同的速度向前移动。
当两个结点相遇时，就是环的入口。
那么，如何求链表在环内的长度呢？
设置快慢指针，快指针每次向前移动两个指针，慢指针每次移动1次，它们第一次相遇的时候一定是在环内，
然后从第一次相遇后开始计数，直到慢结点再次回到这个位置，那么就是环的长度
"""

class LinkedNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def findEntranceInCircleLinkedList(self, linkedNode):
        n = self.circleLength(linkedNode)
        p1, p2 = linkedNode, linkedNode
        while n:
            p2 = p2.next
            n-=1
        while p1!=p2:
            p1 = p1.next
            p2 = p2.next
        return p1
    
    def circleLength(self, linkedNode):
        p1 = linkedNode
        p2 = linkedNode
        p1 = p1.next
        p2 = p2.next.next
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next.next
        
        count = 1
        cur = p1
        p1 = p1.next
        while cur!=p1:
            p1 = p1.next
            count += 1
        return count
            
        

if __name__ == "__main__":
    s = Solution()
    start_node = LinkedNode(3)
    linked = LinkedNode(1)
    linked.next = LinkedNode(2)
    linked.next.next = start_node
    linked.next.next.next = LinkedNode(4)
    linked.next.next.next.next = LinkedNode(5)
    linked.next.next.next.next.next = LinkedNode(6)
    linked.next.next.next.next.next.next = start_node
    print(s.findEntranceInCircleLinkedList(linked).val)