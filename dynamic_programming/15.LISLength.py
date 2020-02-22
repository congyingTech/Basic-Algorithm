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
                if nums[i]>nums[j]:
                    res[i] = max(res[i], res[j]+1)
        return max(res)

    def listOfLIS(self, nums):
        """
        求出最长上升子序列是什么？（boss直聘一面算法题）
        """
        n = len(nums)
        m = [0]*n
        for x in range(n-2,-1,-1):
            for y in range(n-1,x,-1):
                if nums[x] < nums[y] and m[x] <= m[y]:
                    m[x] += 1
            max_value = max(m)
            result = []
            for i in range(n):
                if m[i] == max_value:
                    result.append(nums[i])
                    max_value -= 1
        return result


    def findNumberOfLIS(self, nums):
        """
        求最长上升子序列的个数
        """
        pass

if __name__ == "__main__":
    s = Solution()
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    print(s.listOfLIS(arr))


