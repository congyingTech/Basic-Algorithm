"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

 
示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1
 

提示：

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

进阶：

你可以设计时间复杂度为 O(n2) 的解决方案吗？
你能将算法的时间复杂度降低到 O(n log(n)) 吗?


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence

dp的思想：
定义 dp[i] 为考虑前i个元素，以第i个数字结尾的最长上升子序列的长度，
dp[i] = dp[j] + 1 if nums[j] < nums[i] and 1 <= j < i
MAX_LEN = max(dp[i]) 0<=i<n

其实就是暴力的双重循环，第一层循环是遍历找到以i为结尾的最长上升子序列
第二层循环是具体的找到以i为结尾的最长上升子序列

"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        dp = []
        for i in range(n):
            dp.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        print(dp)
        return max(dp)


if __name__ == "__main__":
    s = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(s.lengthOfLIS(nums))
