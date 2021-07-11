#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-07-12 01:30
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        n = len(citations)
        for i in range(n):
            if citations[i] >= n-i:
                 return n-i
        return 0


if __name__ == "__main__":
    print(Solution().hIndex([0,0]))
