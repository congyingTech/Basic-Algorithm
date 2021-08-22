#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-14 10:43

对于A，B操作可以归为几种：
1）B插入——dp[i-1][j]+1
2）A插入——dp[i][j-1]+1
3）修改A

dp[i][j]表示i长度的A和j长度的B的编辑距离
当S[i] == S[j]时：
   dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1]dp[j-1])

当S[i] != S[j]时：
   dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1]dp[j-1]+1)

而且要注意边界条件

tips:当i和j表示一段长度的时候，那么i的最大值是m+1，j的最大值是n+1
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]-1)
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        return dp[-1][-1]