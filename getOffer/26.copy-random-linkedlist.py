# encoding:utf-8
"""
问题描述：复杂链表的复制
解决方案：
1）主链表上节点的复制
2）random节点的指向复制
3）主链表与复制链表的拆离
"""
class RandomLinkedList(object):
    def __init__(self,val):
        self.val = val
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomLinkedList(self, head):
        pre = head
        # 1)主链表上节点的复制
        while pre:
            copy_node = RandomLinkedList(pre.val)
            next_node = pre.next
            pre.next = copy_node
            copy_node.next = next_node
            pre = next_node
        self.printLinkedList(head)
        # 2)random节点指向复制
        pre = head
        while pre:
            if pre.random:
                pre.next.random = pre.random.next
            pre = pre.next.next
        # 3)原链表与复制链表的拆离
        pre = head.next
        cur_linked_list = pre
        while pre.next:
            pre.next = pre.next.next
            pre = pre.next
        return cur_linked_list

    def printLinkedList(self, head):
        while head:
            print(head.val)
            head = head.next
    


if __name__ == "__main__":
    s = Solution()
    node1 = RandomLinkedList(1)
    node2 = RandomLinkedList(2)
    node3 = RandomLinkedList(3)
    node4 = RandomLinkedList(4)
    node5 = RandomLinkedList(5)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    node1.random = node3
    node2.random = node4

    s.copyRandomLinkedList(node1)
