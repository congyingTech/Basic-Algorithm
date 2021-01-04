# encoding:utf-8
# 问题描述：最长上升子序列的长度
# 解决方案：对于第n个数，两种情况，组成最长上升子序列，不组成最长上升子序列
# dp[n]是第n个数时的最长子序列长度
# 如果
# dp[n] = max(dp[n], dp[j]+1) 0<=j<=n-1

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<1:
            return 0
        arr_len = len(nums)
        res = [1]*arr_len
        for i in range(1, arr_len):
            for j in range(i):
                if nums[i]<nums[j]:
                    res[i] = max(res[i], res[j]+1)
        return max(res)


if __name__ == "__main__":
    s = Solution()
    arr = [-2,-1]
    print(s.lengthOfLIS(arr))
