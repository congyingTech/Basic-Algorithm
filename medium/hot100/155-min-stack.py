#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-21 01:50
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sta = []
        self.minsta = [float('inf')]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.sta.append(val)
        self.minsta.append(min(self.minsta[-1], val))
        return None

    def pop(self):
        """
        :rtype: None
        """
        self.sta.pop()
        self.minsta.pop()
        return None

    def top(self):
        """
        :rtype: int
        """
        return self.sta[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minsta[-1]
