# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 11:02 上午
# @Author  : Mohn
# @FileName: 76-minimum-window-substring.py
"""
76. 最小覆盖子串
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

滑动窗口：
l/r指针滑动窗口的方法: r一直往右移动，直到t在s中，停止移动。这时候l向右移动，直到t不在s中。
和getOffer/65题一样都是滑动窗口的方法。
"""


class Solution(object):

    def check(self, a, b):

        for i in a:
            if i not in b:
                return False
            else:
                b = b.replace(i, '', 1)
        return True

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ''
        if len(s) == len(t):
            if self.check(s, t):
                return s
            else:
                return ''
        # 滑动窗口的l和r指针
        l, r = 0, 1
        n = len(s)
        min_cover_len = float('inf')
        min_str = ''
        flag = False
        while l <= n and r <= n and l <= r:
            slide_s = s[l:r]
            while r <= n and not self.check(t, slide_s):
                r += 1
                slide_s = s[l:r]
            while l <= r and self.check(t, slide_s):
                l += 1
                slide_s = s[l:r]
                flag = True
            if flag and min_cover_len > r-l+1:
                min_str = s[l-1:r]
                min_cover_len = r-l+1
        return min_str


if __name__ == "__main__":
    s1 = Solution()

    s = "ab"
    t = "ba"
    # s = "ADOBECODEBANC"
    # t = "ABC"
    print(s1.minWindow(s, t))
