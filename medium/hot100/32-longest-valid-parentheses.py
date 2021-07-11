#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-07-11 22:56

最长有效括号长度
dp[i]表示第i位的最长括号长度
if s[i] == ')' and s[i-1] == '(':
    dp[i] = dp[i-2] + 2

if s[i] == ')' and s[i-1] == ')':
    if s[i - dp[i-1] -1] == '(':
        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]



"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0] * n
        res = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2

                elif s[i-1] == ')' and i-dp[i-1]-1 >= 0:
                    if s[i-dp[i-1]-1] == '(':
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]

            res = max(res, dp[i])
        return res


if __name__ == "__main__":
    s = Solution()
    s1 = "()()"
    print(s.longestValidParentheses(s1))
