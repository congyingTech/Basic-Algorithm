#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-21 22:45

将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

原始字符串：PAYPALISHIRING
z字型书写：
P   A   H   N
A P L S I I G
Y   I   R
产出字符串：
按行读取：PAHNAPLSIIGYIR
"""


class Solution(object):
    def convert(self, s, numRows):
        res = ["" for _ in range(numRows)]
        i = 0
        gap = -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows-1:
                gap = -gap
            i += gap
        return "".join(res)


if __name__ == "__main__":
    s = 'PAYPALISHIRING'
    print(Solution().convert(s, 3))
