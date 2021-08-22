# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 7:43 下午
# @Author  : Mohn
# @FileName: *10-regular-expression-matching.py
"""
动态规划：
dp[i][j]表示s前i个字符串和p的前j个字符串可以match
其中i和j也表示的长度
如果p[j-1]是字符或者.
if s[i-1]==p[j-1] or p[j-1]=='.':
    dp[i][j] = dp[i-1][j-1]
else:
    return False

如果p[j-1]是*
if s[i-1] == p[j-2]:
    dp[i][j] = dp[i][j-2] or dp[i-1][j]
s[i-1]!=p[i-2]:
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
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True

        for i in range(m+1):
            for j in range(1, n+1):
                # 如果p[j-1]是字符或者是.的情况
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                # 如果p[j-1]是*的情况
                elif p[j-1] == "*":
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                    elif s[i-1] != p[j-2]:
                        dp[i][j] = dp[i][j-2]
        return dp[-1][-1]


if __name__ == "__main__":
    s = "aaa"

    p = "aaaa"
    a = Solution()
    print(a.isMatch(s, p))
