#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-10 23:32

跳跃游戏2：每次可以跳<=nums[i]的步数，求跳到终点的最小步数
动态规划的解法
"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [9999 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 0
        # dp[i+j] = min(dp[i+j], dp[i]+1)
        i = 1
        while i <= n:
            j = 1  # 每次都要遍历所有的路径可能性
            while j <= nums[i-1] and i+j <= n:
                dp[i+j] = min(dp[i+j], dp[i]+1)
                j += 1
            i += 1
        return dp[-1]
