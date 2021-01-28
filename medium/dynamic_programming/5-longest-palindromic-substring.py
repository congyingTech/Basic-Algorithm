#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-01-28 09:17

给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"
示例 4：

输入：s = "ac"
输出："a"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring

dp思路：
最长回文子串的三种情况
dp[i][j]表示从i到j是否是最长回文子串,那么需要i+1:j-1是回文子串
dp[i][j] = dp[i+1][j-1] and s[i]==s[j] j>i+2时
dp[i][j] = s[i]==s[j] i<j<=i+2时
dp[i][j] = 1 i=j时

"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        dp[0][0] = True
        max_gap_ind = [0, 0]
        # cababaad
        for i in range(n):
            for j in range(i, n):
                if j > i+2:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                elif i < j <= i+2:
                    dp[i][j] = s[i] == s[j]
                elif i == j:
                    dp[i][j] = True
                if dp[i][j]:
                    max_gap = max_gap_ind[1] - max_gap_ind[0]
                    if j-i > max_gap:
                        max_gap_ind[0] = i
                        max_gap_ind[1] = j
        return s[max_gap_ind[0]: max_gap_ind[1]-1]


if __name__ == "__main__":
    s = Solution()
    st = "cababaad"
    print(s.longestPalindrome(st))

