#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-13 00:21

对比第5题，最长回文子串
子串必须是连续的，子序列未必是连续的
同样dp[i][j]表示从s到j最长回文子序列的长度
当s[i] = s[j]时：
dp[i][j] = dp[i+1][j-1] + 2
当s[i] != s[j]时：
dp[i][j] = max(dp[i+1][j], dp[i][j-1])

i+1这种的一定是自底向上

"""


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        res = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                #                elif j==i+1:
                #                    if s[i] == s[j]:
                #                        dp[i][j] = 2
                #                    else:
                #                        dp[i][j] = 1
                elif j >= i + 1:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                    else:
                        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                res = max(res, dp[i][j])
        return res

