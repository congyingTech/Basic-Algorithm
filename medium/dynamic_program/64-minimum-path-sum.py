"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum

dp思想：
dp[i][j] = min(dp[i-1][j], dp[i][j-1])+dp[i][j] i>0, j>0
dp[i][j] = dp[i][j-1]+grid[i][j-1] i=0, j>0 # 第一行
dp[i][j] = dp[i-1][j]+grid[i-1][j], i>0, j=0 # 第一列
dp[0][0] = grid[0][0]
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif i > 0 and j == 0:
                    dp[i][j] = dp[i-1][j]+grid[i][j]
                else:
                    continue
        return dp[m-1][n-1]


if __name__ == "__main__":
    s = Solution()
    grid = [[1,2,3],[4,5,6]]
    print(s.minPathSum(grid))
