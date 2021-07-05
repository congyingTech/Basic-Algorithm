# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 7:24 下午
# @Author  : Mohn
# @FileName: 31-next-permutation.py
"""
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须 原地 修改，只允许使用额外常数空间。
nums = [1,2,3]->[1,3,2]
nums = [3,2,1]->[1,2,3]
nums = [1,1,5]->[1,5,1]
 [4,5,2,6,3,1]
 step1:较小数2
 step2:较大数3
 step3:交换->453621
 step4:排序->453126
1.寻找较小数:从后往前，找到nums[i]<nums[i+1],那么，nums[i]一定是较小数；
2.寻找较大数:在[i+1, n]区间上，从后往前，找到nums[j]>nums[i]，那么nums[j]一定是较大数；
3.交换
3.较小数位置[i+1,n]区间上本身一定是降序的，进行双指针逆序排序，交换指针的位置。
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums


if __name__ == "__main__":
    s = Solution()
    nums = [3,2,1]
    print(s.nextPermutation(nums))
