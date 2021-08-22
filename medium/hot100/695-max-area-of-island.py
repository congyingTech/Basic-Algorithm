#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-14 10:14

最大岛屿面积：dfs求每个位置的面积，然后比较出来最大的那个
"""


class Solution(object):

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != 1:
            return 0
        grid[i][j] = 0
        ans = 1
        for gap_i, gap_j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            next_i, next_j = i + gap_i, j + gap_j
            ans += self.dfs(grid, next_i, next_j)
        return ans

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(self.dfs(grid, i, j), ans)
        return ans