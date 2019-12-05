# -*- coding:utf-8 -*-

# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

class Solution:
    def jumpFloor(self, number):
        lists = []
        result = 1
        if number == 0:
            return 0
        if number == 1:
            return result
        lists.append(result)
        lists.append(result)
        i = 2
        while i <= number:
            lists.append(lists[i - 1] + lists[i - 2])
            i += 1
        return lists[i - 1]


if __name__ == "__main__":
    # s = Solution()
    # print(s.Fibonacci(5))
    s1 = Solution()
    print(s1.jumpFloor(3))
