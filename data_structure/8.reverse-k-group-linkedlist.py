# encoding:utf-8

class LinkedList(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def reverseKGroup(self, linkedlist, k):
        if not linkedlist:
            return 
        temp = linkedlist
        for _ in range(k):
            if temp.next:
                temp = temp.next
        if not temp:
            return linkedlist
        t2 = temp.next
        temp.next = None
        newLinkedlist = self.reverseLinkedList(linkedlist)
        temp.next = self.reverseKGroup(t2, k)
        return newLinkedlist

    def reverseLinkedList(self, linkedlist):
        if not linkedlist:
            return None
        pre = linkedlist
        cur = pre.next
        pre.next = None
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur 
            cur = next_node
        return pre

if __name__ == "__main__":
    s = Solution()
    k=3
    linkedlist = LinkedList(1)
    linkedlist.next = LinkedList(2)
    linkedlist.next.next = LinkedList(3)
    linkedlist.next.next.next = LinkedList(4)
    linkedlist.next.next.next.next = LinkedList(5)
    linkedlist.next.next.next.next.next = LinkedList(6)
    linkedlist.next.next.next.next.next.next = LinkedList(7)
    
    kgroupreversed = s.reverseKGroup(linkedlist, k)
    while kgroupreversed:
        print(kgroupreversed.val)
        kgroupreversed = kgroupreversed.next