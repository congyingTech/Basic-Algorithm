# -*- coding: utf-8 -*-
# @Time    : 2021/9/16 3:01 下午
# @Author  : Mohn
# @FileName: 416-partition-equal-subset-sum.py

"""
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。

np难的问题，dp的思路，
重点：i表示nums的下标，j表示目前数组中选取的元素和
0<=i<n
0<=j<=target

为什么会分j>=nums[i]和j<nums[i]两种情况呢？
因为dp的列的下标需要>=0,当小于0的时候nums[i]是不可以加入的
所以 当 j-nums[i]>=0,j>=nums[i] 时：nums[i]有加入和不加入两种选择

当j>=nums[i]时，
说明nums[i]处于可以加入的状态,那么分两种情况
（1）nums[i]加入：dp[i][j] = dp[i-1][j-nums[i]]
（2）nums[i]不加入：dp[i][j] = dp[i-1][j]

当j<nums[i]时，
说明nums[i]处于不可加入的状态
dp[i][j] = dp[i-1][j]

"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        maxNum = max(nums)
        nums_sum = sum(nums)
        is_odd = nums_sum % 2
        if is_odd:
            return False
        target = nums_sum // 2
        if maxNum > target:
            return False
        # 初始化dp
        dp = [[False]*(target+1) for _ in range(len(nums))]

        # 边界条件设置——0行0列进行特殊处理
        # target是0的时候，无论遍历到任何一个元素，只要不选取就可以实现，所以都是True
        for i in range(len(nums)):
            dp[i][0] = True
        # 当遍历到第一个元素的时候，这时候只能选取一个元素，所以target一定是nums[0]
        dp[0][nums[0]] = True

        for i in range(1, len(nums)):
            for j in range(1, target+1):
                if j-nums[i] >= 0:
                    dp[i][j] = dp[i-1][j-nums[i]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[len(nums)-1][target]


if __name__ == "__main__":
    print(Solution().canPartition([1, 2, 3, 4, 5, 6, 7]))
