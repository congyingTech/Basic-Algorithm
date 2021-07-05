# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 7:43 下午
# @Author  : Mohn
# @FileName: 10-regular-expression-matching.py
"""
动态规划：
dp[i][j]表示s前i个字符串和p的前j个字符串可以match
如果p[j]是字符或者.
if s[i]==p[j] or p[j]=='.':
    dp[i][j] = dp[i-1][j-1]
else:
    return False

如果p[j]是*
if s[i] == p[j-1]:
    dp[i][j] = dp[i][j-2] or dp[i-1][j]
s[i]!=p[i-1]:
    dp[i][j] = dp[i][j-2]

"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        dp = [[False for _ in range(n)] for _ in range(m)]
        dp[0][0] = True
        for j in range(n):
            dp[0][j] = True
        for i in range(1, m):
            for j in range(1, n):
                if s[i] == p[j] or p[j] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == "*":
                    if s[i] == p[j-1] or p[j-1] == '.':
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                    elif s[i] != p[j-1]:
                        dp[i][j] = dp[i][j-2]
        return dp[-1][-1]


if __name__ == "__main__":
    s = "aaa"

    p = "aaaa"
    a = Solution()
    print(a.isMatch(s, p))
