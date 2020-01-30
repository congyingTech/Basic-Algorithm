# encoding:utf-8
"""
问题描述：合并两个上升排序的链表，使之合并后有序
解决方案：递归的方案，
非递归的方案:先比较第一个节点，节点小的那一个作为主链表，把循环遍历另一条链表，把其中的元素插入到主链表中
在主链表设置两个指针：mainHead/mainNext，次链表只有secondHead一个指针，做次链表单节点插入主链表的动作。
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val < l2.val:
            mainHead = l1
            secondHead = l2
        else:
            mainHead = l2
            secondHead = l1
        mainNext = mainHead.next
        mergeHead = mainHead
        while secondHead:
            if not mainNext:
                mainHead.next =  secondHead
                break
            # 当第二个linkedlist的node的值小于主list的时候，把其插入主list
            if secondHead.val<mainNext.val:
                mainHead.next = secondHead
                secondHead = secondHead.next
                mainHead.next.next = mainNext
                mainHead = mainHead.next
            else:
                mainHead = mainHead.next
                mainNext = mainNext.next
        
        return mergeHead
    def printLinkList(self, head):
        while head:
            print(head.val)
            head = head.next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val<l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def printLinkList(self, head):
        while head:
            print(head.val)
            head = head.next



if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    # l1.next.next.next = ListNode(7)
    # l1.next.next.next.next = ListNode(9)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    # l2.next.next.next = ListNode(8)
    # # 递归的方法
    # l = s.mergeTwoLists(l1, l2)
    # s.printLinkList(l)

    s1 = Solution1()
    l1 = s1.mergeTwoLists(l1,l2)
    s1.printLinkList(l1)