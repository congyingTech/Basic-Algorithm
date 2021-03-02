"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers

解题思路：
每个数位都是逆序的，所以可以从头遍历两个链表，把两个链表的值相加
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        res_Node = ListNode()
        head_res = res_Node
        temp = 0
        while p1 or p2 or temp:
            if p1 and not p2:
                res_val = p1.val + temp
            elif not p1 and p2:
                res_val = p2.val + temp
            elif p1 and p2:
                res_val = p1.val + p2.val + temp
            elif not p1 and not p2 and temp:
                res_val = temp
            else:
                break
            temp = 0

            if res_val < 10:
                res = ListNode(res_val)
            else:
                res = ListNode(res_val % 10)
                temp = res_val // 10
            head_res.next = res
            head_res = head_res.next

            if p1 and p1.next:
                p1 = p1.next
            else:
                p1 = None

            if p2 and p2.next:
                p2 = p2.next
            else:
                p2 = None
        res = res_Node.next

        return res


if __name__ == "__main__":
    s = Solution()
    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    l1_node = ListNode(l1[0])
    p1 = l1_node
    l2_node = ListNode(l2[0])
    p2 = l2_node
    for i in range(1, len(l1)):
        p1.next = ListNode(l1[i])
        p1 = p1.next
    for i in range(1, len(l2)):
        p2.next = ListNode(l2[i])
        p2 = p2.next
    s.addTwoNumbers(l1_node, l2_node)
