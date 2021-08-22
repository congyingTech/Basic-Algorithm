#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-22 12:39
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        minF = maxF = ans = nums[0]
        for i in range(1, n):
            minf = minF
            maxf = maxF
            maxF = max(max(maxf*nums[i], nums[i]), minf*nums[i])
            minF = min(min(minf*nums[i], nums[i]), maxf*nums[i])
            ans = max(maxF, ans)
        return ans
