# -*- coding: utf-8 -*-
# @Time    : 2021/6/22 2:38 下午
# @Author  : Mohn
# @FileName: 11-container-with-most-water.py

"""
解题思路：左右双指针
maxArea = min(p, q) * p和q的间距
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        p = 0
        q = len(height)-1
        max_area = 0
        while p != q:
            max_area = max(min(height[p], height[q])*(q - p), max_area)
            if height[p] < height[q]:
                p += 1
            else:
                q -= 1
        return max_area


if __name__ == "__main__":
    s = Solution()
    height = []
    print(s.maxArea(height))
