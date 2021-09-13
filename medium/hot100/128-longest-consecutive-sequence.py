# -*- coding: utf-8 -*-
# @Time    : 2021/9/13 3:21 下午
# @Author  : Mohn
# @FileName: 128-longest-consecutive-sequence.py
"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-consecutive-sequence
[100,4,200,1,3,2]
最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4
输出是4
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_streak = 0
        num_set = set(nums)
        for num in num_set:
            if num-1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num+1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak


if __name__ == "__main__":
    s = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    s.longestConsecutive(nums)
