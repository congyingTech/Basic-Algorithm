#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-14 16:40
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def binarySearch(nums, target, flag):
            left = 0
            right = len(nums) - 1
            ans = len(nums) - 1
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] > target or (flag and nums[mid] >= target):
                    right = mid-1
                    ans = mid
                else:
                    left = mid+1

            return ans
        if not nums:
            return [-1, -1]
        right_index = binarySearch(nums, target, False) - 1
        left_index = binarySearch(nums, target, True)

        if left_index<=right_index and right_index<len(nums) and nums[left_index]==target and nums[right_index]==target:
            return [left_index, right_index]
        return [-1, -1]


if __name__ == "__main__":
    print(Solution().searchRange([5,7,7,8,8,10], 8))