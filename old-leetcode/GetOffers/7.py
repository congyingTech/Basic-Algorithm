# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
# n<=39

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n == 0 or n>39 or n == 1:
            return 1
        return self.Fibonacci(n-1)+self.Fibonacci(n-2)

class Solution:
    def Fibonacci(self, n):
        if n == 0 or n>39 or n == 1:
            return 1
        return self.Fibonacci(n-1)+self.Fibonacci(n-2)

class Solution1:
    def Fibonacci(self, n):
        lists = []
        result = 1
        if n == 0:
            return 0
        if n == 1 :
            return result
        lists.append(0)
        lists.append(result)
        i = 2
        while i <= n:
            lists.append(lists[i-1]+lists[i-2])
            i += 1
        return lists[i-1],lists


if __name__ == "__main__":
    #s = Solution()
    #print(s.Fibonacci(5))
    s1 = Solution1()
    print(s1.Fibonacci(9))