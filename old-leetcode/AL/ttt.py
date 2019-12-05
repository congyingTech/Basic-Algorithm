#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2019-11-26 11:35
"""


class Solution(object):

    def isSafe(self, visit_record_i, pos, n):
        if visit_record_i==False and pos<n:
            return True

    def backtiles(self, array, temp, res, pos, visit_record, n):
        if temp not in res and temp:
            #inner = temp.copy()
            res.add(temp)
        if pos == n:
            return
        for i in range(n):
            if self.isSafe(visit_record[i], pos, n):
                temp += array[i]
                visit_record[i] = True
                self.backtiles(array, temp, res, pos+1, visit_record, n)
                visit_record[i] = False
                temp = temp[:-1]

    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        temp = ''
        res = set()
        #array = list(tiles)
        n = len(tiles)
        visit_record = [False]*n
        self.backtiles(tiles, temp, res, 0, visit_record, n)
        return len(res)


if __name__ == "__main__":
    s = Solution()
    res = s.numTilePossibilities('AAB')
    print(res)
