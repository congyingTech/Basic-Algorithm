#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-10 23:35
跳跃游戏1：在i位置可以跳<=nums[i]的步数，判断是否可以到达最后一个下标

贪心的思路：遍历每一个元素，当前i元素，能抵达的最远距离是max(most_index, i+num[i])
如果这个最远距离大于等于数组的长度，则一定可以抵达终点
记住i<=most_index

"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        most_index = 0
        for i, num in enumerate(nums):
            if i <= most_index:
                most_index = max(most_index, i+num)
                if most_index >= len(nums)-1:
                    return True
        return False
