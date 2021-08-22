#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-13 00:10

找出柱状图中最大的矩形面积
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        i = 0
        max_area = 0
        sta = []
        while i < n:
            # 如果i位置的高度大于单调增栈的高度，那么继续记录单调增栈
            if not sta or heights[i] >= sta[-1]:
                sta.append(heights[i])
                i += 1
            #  否则开始pop单调增栈，计算最大的面积, 此时i不动
            else:
                k = sta.pop()
                max_area = max(max_area, heights[k]*(i-sta[-1]-1 if sta else i))

        while sta:
            k = sta.pop()
            max_area = max(max_area, heights[k]*(i-sta[-1]-1 if sta else i))
        return max_area
