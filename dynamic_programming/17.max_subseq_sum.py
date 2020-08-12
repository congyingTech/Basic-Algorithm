# encoding:utf-8
"""
问题描述：最大连续子序列的和
解决方案：如果当前的num是正数，那么就加入，否则不加入
dp[i] = nums[i] if dp[i-1] < 0  else dp[i] = dp[i-1]+nums[i]
"""
class Solution(object):
    def maxSubseqSum(self, nums):
        res = [0]*len(nums)
        res[0] = nums[0]
        for i in range(1, len(nums)):
            if res[i-1]<0:
                res[i] = nums[i]
            else:
                res[i] = res[i-1]+nums[i]
        print(res[-1])

if __name__ == "__main__":
    s = Solution()
    nums = [1,3,4,-9,8,10]
    s.maxSubseqSum(nums)