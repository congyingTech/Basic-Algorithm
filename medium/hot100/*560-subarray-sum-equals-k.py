# -*- coding: utf-8 -*-
# @Time    : 2021/9/13 7:33 下午
# @Author  : Mohn
# @FileName: 560-subarray-sum-equals-k.py
"""
给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。
pre[i]代表第i位的前缀和,
从j到i的子数组和为k，即pre[i]-pre[j-1] = k
pre[j-1] = pre[i] - k
pre_dict的key是前缀和，value是统计的次数
"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre_dict = dict()
        pre_dict[0] = 1
        n = len(nums)
        pre = 0
        count = 0
        for i in range(n):
            pre += nums[i]
            if pre-k in pre_dict.keys():
                count += pre_dict.get(pre-k)
            pre_dict[pre] = pre_dict.get(pre, 0) + 1
        return count


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 1, 2, -1, 3]
    k = 2
    print(s.subarraySum(nums, k))
