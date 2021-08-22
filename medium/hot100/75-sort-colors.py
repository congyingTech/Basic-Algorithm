#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-17 22:58


双指针的办法：
如果元素是0，p0和nums[i]进行交换，在此基础上，如果p0<p1则p1和nums[i]交换，移动两个指针
如果元素是1，则只移动p1，然后交换i位置的num和p1位置的num
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p0 = p1 = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1
            elif nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1

        return nums
