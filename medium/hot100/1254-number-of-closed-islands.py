# -*- coding: utf-8 -*-
# @Time    : 2021/11/2 11:37 上午
# @Author  : Mohn
# @FileName: 1254-number-of-closed-islands.py
"""
相较于第200题，只是在周边的地方都必须是海水了，这里面1是海水，0是陆地
"""


class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        m = len(grid)
        n = len(grid[0])

        # 相较于200题，把周边的地方都填平成海
        for i in range(m):
            self.dfs(grid, i, 0)
            self.dfs(grid, i, n-1)

        for j in range(n):
            self.dfs(grid, 0, j)
            self.dfs(grid, m-1, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans += 1
                    self.dfs(grid, i, j)
        return ans

    # dfs负责把陆地变成海水，避免重复计数
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 1:
            return
        grid[i][j] = 1
        for gap_i, gap_j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            next_i, next_j = i + gap_i, j + gap_j
            self.dfs(grid, next_i, next_j)


if __name__ == "__main__":
    s = Solution()
    grid = [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]]

    print(s.closedIsland(grid))
