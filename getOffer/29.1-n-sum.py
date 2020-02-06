# encoding:utf-8
"""
问题描述：
求1+2+....+n，要求不能使用乘除法，for while if else switch等关键字
解决方案：
递归的解法：f(n) = n+f(n-1)
"""


class Solution(object):
    def getSum(self, n):
        if n<0:
            return 0
        return n + self.getSum(n-1)

if __name__ == "__main__":
    s = Solution()
    n = 10
    print(sum([i for i in range(11)]))
    print(s.getSum(n))