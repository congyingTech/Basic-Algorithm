# encoding:utf-8
"""
问题描述：一个数组里面有正数和负数， 求连续子序列的最大的和值。要求时间复杂度为O(N)
解决方案：
动态规划的解法, dp[i]表示遍历到第i个元素的时候以i结尾的数组的最大和，
对于第i个元素无非有两种选择：1）前i-1个元素的数组的最大和加入，此时dp[i-1]>0；2）前i-1个元素的数组的最大和不加入,此时dp[i-1]<=0

"""

class Solution(object):
    def findMaxConArrSum(self, arr):
        n = len(arr)
        dp = [0] * n
        dp[0] = arr[0]
        for i in range(1, n):
            temp1 = dp[i-1] + arr[i]
            temp2 = arr[i]
            dp[i] = max(temp1, temp2)
        return max(dp)

if __name__ == "__main__":
    s = Solution()
    arr = [-1,2,3,-5,1,5,9]
    print(s.findMaxConArrSum(arr))