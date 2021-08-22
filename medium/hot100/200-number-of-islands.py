#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-14 10:34

岛屿的数量：当遇到1的时候，就用dfs把上下左右为1的部分全部置为0，这样不会重复计算，然后一个个的计算岛屿面积
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
                return
            grid[i][j] = '0'
            for gap_i, gap_j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                next_i, next_j = i + gap_i, j + gap_j
                dfs(grid, next_i, next_j)

        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(grid, i, j)

        return ans


if __name__ == "__main__":
    s = Solution()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(s.numIslands(grid))
