# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        for i in range(0, 32):
            if(n&1 == 1):
                count += 1
            n = n >> 1
            #print(n)
        return count
if __name__ == "__main__":
    # s = Solution()
    # print(s.Fibonacci(5))
    s = Solution()
    print(s.NumberOf1(7))