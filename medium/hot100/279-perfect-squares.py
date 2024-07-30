# -*- coding: utf-8 -*-
# @Time    : 2021/10/21 2:53 下午
# @Author  : Mohn
# @FileName: 279-perfect-squares.py
"""
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

动态规划思路：
dp[i]表示和为i的最小的完全平方数数量
dp[i] = min(dp[i], dp[i-square_num]+1)

"""
import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        square_nums = [i**2 for i in range(int(math.sqrt(n))+1)]
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for square_num in square_nums:
                if i < square_num:
                    break
                dp[i] = min(dp[i], dp[i-square_num]+1)
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    n = 11
    print(s.numSquares(n))

