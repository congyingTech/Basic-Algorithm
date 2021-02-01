"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物，障碍物用1来表示，0表示空网格。那么从左上角到右下角将会有多少条不同的路径？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii

dp思路：
问总共有多少条不同的路径？
dp[i][j]表示到达坐标i，j的时候有多少条路径，当有障碍物的时候，就无法抵达dp[i][j]=1

dp[0][0] = 1
if grid[i][j]==1:
   dp[i][j]=0
else:
   dp[i][j] = dp[i-1][j] + dp[i][j-1] i>0 j>0
   dp[i][j] = dp[i][j-1] i=0, j>0
   dp[i][j] = dp[i-1][j] j=0, i>0

"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i-1][j]
                elif i > 0 and j > 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    continue
        return dp[m-1][n-1]


if __name__ == "__main__":
    s = Solution()
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(s.uniquePathsWithObstacles(obstacleGrid))
