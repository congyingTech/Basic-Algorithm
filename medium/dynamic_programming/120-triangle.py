"""
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

 

示例 1：

输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
dp的思想：
dp[i][j]表示处于i层j个的时候的最小路径和
dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)+1
        dp = [[0]*j for j in range(1, m)]
        dp[0][0] = triangle[0][0]
        for i in range(1, m-1):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]

        for i in range(2, m):
            for j in range(2, i+1):
                if j >= 2 and i >= 2:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

        return dp[m-1][m-1]


if __name__ == "__main__":
    s = Solution()
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(s.minimumTotal(triangle))
