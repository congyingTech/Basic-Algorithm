#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-17 00:11

Boyer-Moore 投票算法

"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            if count <= 0:
                candidate = num
                count = 0
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
