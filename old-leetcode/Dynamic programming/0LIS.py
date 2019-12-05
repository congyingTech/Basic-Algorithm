#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2019-06-18 16:52
"""


def lis(a):
    dp = [0]
    for i in a:
        if i > dp[-1]:
            dp.append(i)
            dp1 = dp
        else:
            dp1 = dp
        dp = max(len(dp1), len(dp))
    return dp


if __name__ == "__main__":
    a = [1, 5, 3, 4, 6, 9, 7, 8]
    dp = lis(a)
    print(dp)
