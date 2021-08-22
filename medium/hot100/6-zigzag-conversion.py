#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-21 22:45
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
        return res
