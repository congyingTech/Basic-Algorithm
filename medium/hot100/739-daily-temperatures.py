#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-21 13:08

思路：sta是个单调递减栈，栈内存放的是元素的下标
"""


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        sta = [0]  # 单调下降栈
        n = len(temperatures)
        ans = [0] * n
        for i in range(1, n):
            while sta and temperatures[i] > temperatures[sta[-1]]:
                pop_index = sta.pop()
                ans[pop_index] = i - pop_index
            sta.append(i)
        return ans
