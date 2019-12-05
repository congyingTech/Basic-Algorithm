#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2019-08-27 10:53
"""
s = 'abc'

for c1 in range(0, 3):
    for c2 in range(0, 3):
        for c3 in range(0, 3):
            print(s[c1]+s[c2]+s[c3])

