# -*- coding: utf-8 -*-
# @Time    : 2021/10/26 2:01 下午
# @Author  : Mohn
# @FileName: 221-maximal-square.py
"""
矩阵中组成的最大的正方形的面积
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-square


动态规划的思想：
dp[i][j]表示以i，j为右下角的元素组成的最大的正方形的边长，dp[i][j]跟它左边，上边，左上角位置的最小的dp有关系
所以，dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 行
        rows = len(matrix)
        # 列
        columns = len(matrix[0])
        maxSide = 0
        dp = [[0]*columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        maxArea = maxSide*maxSide
        return maxArea


if __name__ == "__main__":
    s = Solution()
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    print(s.maximalSquare(matrix))
