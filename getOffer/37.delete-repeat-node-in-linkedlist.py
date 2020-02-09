# encoding:utf-8
"""
问题描述：
在一个排序链表中，如何删除所有的重复的结点？
解决方案：
设置两个结点，然后从头遍历，看相邻的两个结点是否相同，如果相同则删除后一个结点
问题是需要删除所有的重复的结点，所以需要记录pre结点，并在删除后指向不重复的结点

"""

 
class LinkedNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution1(object):
    def deleteAllRepeatNodes(self, linked):
        pre = None
        cur = linked
        nex = linked.next
        while cur:
            flag = False
            while cur.val == nex.val and nex.next:
                cur = cur.next
                nex = nex.next
                flag = True
            if not flag and nex.next:
                pre = cur
            else:
                pre.next = cur
            cur = cur.next
            if nex.next:
                nex = nex.next
            

        return linked


class Solution(object):
    def deleteRepeatNode(self, linked):
        pre = linked
        cur = linked.next
        while cur:
            if pre.val == cur.val:
                nex = cur.next
                pre.next = nex
                cur = nex
            else:
                pre = pre.next
                cur = cur.next
        return linked

if __name__ == "__main__":
    s1 = Solution1()
    linked = LinkedNode(1)
    linked.next = LinkedNode(2)
    linked.next.next = LinkedNode(3)
    linked.next.next.next = LinkedNode(3)
    linked.next.next.next.next = LinkedNode(3)
    linked.next.next.next.next.next = LinkedNode(4)
    linked.next.next.next.next.next.next = LinkedNode(4)
    linked.next.next.next.next.next.next.next = LinkedNode(5)
    linked.next.next.next.next.next.next.next.next = LinkedNode(5)
    s1.deleteAllRepeatNodes(linked)