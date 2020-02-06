# encoding:utf-8
"""
问题描述：
圆圈中最后剩下的数字
解决方案：
循环链表的方法
"""


class CircleNode(object):
    def __init__(self, val):
        self.val = val 
        self.next = None 


class Solution(object):
    def findCircleLastNum(self, circle, m):
        res = []
        p1 = circle
        while p1 and p1.next!=p1:
            time = m
            while time>1:
                p1=p1.next
                time -= 1
            res.append(p1.val)
            # 将后一个结点的值赋给p1，然后删除后一个结点
            temp = p1.next.val
            p1.val = temp
            p1.next = p1.next.next
        print(res)
        print(p1.val)

if __name__ == "__main__":
    s = Solution()
    t1 = CircleNode(1)
    t2 = CircleNode(2)
    t3 = CircleNode(3)
    t4 = CircleNode(4)
    t5 = CircleNode(5)
    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5
    t5.next = t1

    m = 3
    s.findCircleLastNum(t1, m)