#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-21 21:55

和739都属于单调栈类型的题

思路：queue是单调递减队列，队列存放的是元素的下标，单调减指的是元素大小单调减
"""


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        res = []
        queue = []
        for i in range(n):
            if i >= k and i-queue[0] >= k:
                queue.pop(0)
            while queue and nums[queue[-1]] >= nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k-1:
                res.append(nums[queue[0]])
        return res
