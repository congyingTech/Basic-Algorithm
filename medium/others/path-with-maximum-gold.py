# encoding:utf-8
# n*m大小的gold，这个是可以从非0的任意点向左向右向上向下走
# maxGold[i][j] = max(maxGold[i-1][j], maxGold[i][j-1], maxGold[i+1][j], maxGold[i][j+1]) + grid[i][j]
# 边界情况：i=0时，上一个只能从下或者从左或者右边过来，
# i=n-1时，上一个只能从上或者左边或者右边过来
# j=0时，上一个可以从上或从下或从右过来，
# j=m-1时，上一个可以从上或下或左边过来
# 
# 错的。。。这根本不是一个可以通过动态规划求解的问题，为啥呢？
# 不同于gold-mine-problem，该问题的子状态的位置无法确定，走向是上下左右，而后者大方向只想右边走。
# 而且出发点的位置也不同。

class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # n行m列
        n = len(grid)
        m = len(grid[0])
        maxGold = [[0]*m for i in range(n)]

        for j in range(m):
            for i in range(n):
                if i==0 and j==0:
                    maxGold[i][j] = max(maxGold[i][j+1], maxGold[i+1][j])+grid[i][j]
                elif i==0 and j!=0 and j!=m-1:
                    maxGold[i][j] = max(maxGold[i][j+1], maxGold[i+1][j], maxGold[i][j-1])+grid[i][j]
                elif i == n-1 and j==0:
                    maxGold[i][j] = max(maxGold[i-1][j], maxGold[i][j+1])+grid[i][j]
                elif i == n-1 and j!=0 and j!=m-1:
                    maxGold[i][j] = max(maxGold[i-1][j], maxGold[i][j+1], maxGold[i][j-1])+grid[i][j]
                elif i == n-1 and j==m-1:
                    maxGold[i][j] = max(maxGold[i-1][j], maxGold[i][j-1])+grid[i][j]
                elif j == m-1 and i!=0 and i!=n-1:
                    maxGold[i][j] = max(maxGold[i-1][j], maxGold[i+1][j], maxGold[i][j-1])+grid[i][j]
                elif i == 0 and j==m-1:
                    maxGold[i][j] = max(maxGold[i][j-1], maxGold[i+1][j])+grid[i][j]
                elif j==0 and i!=0 and i!=n-1:
                    maxGold[i][j] = max(maxGold[i-1][j], maxGold[i+1][j], maxGold[i][j+1])+grid[i][j]

                else:
                    maxGold[i][j] = max(maxGold[i-1][j], maxGold[i][j-1], maxGold[i+1][j], maxGold[i][j+1]) + grid[i][j]
        print(maxGold)
if __name__ == "__main__":
    s = Solution()
    grid = [[0,6,0],
            [5,8,7],
            [0,9,0]]
    s.getMaximumGold(grid)