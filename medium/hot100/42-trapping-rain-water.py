#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-07-05 23:35

暴力法：
和11题不同的是，42题是柱子，11题是垂线，柱子的情况下，需要遍历柱子计算面积

遍历每个柱，第i个柱上方接水最多area = min(max(height[:i-1]), max(height[i+1:])) - height[i]

动态法1：
时间/空间复杂度O(n)
转移方程
过去：正序找出所有的leftMax, leftMax[i] = max(leftMax[i-1], height[i])
未来：逆序找出所有的rightMax, rightMax[i] = max(rightMax[i+1], height[i])

动态+双指针：
双指针left， right代替leftMax和rightMax两个数组

"""


class Solution(object):
    def trap1(self, height):
        """
        暴力-超时
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        area = 0
        for i in range(1, n-1):
            cur_h = height[i]
            max_left = max(height[:i])
            max_right = max(height[i:])
            area += max(0, min(max_left, max_right) - cur_h)
        return area

    def trap2(self, height):
        # 动态规划
        n = len(height)
        leftMax = [height[0]] + [0] * (n-1)
        rightMax = [0] * (n-1) + [height[n-1]]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i])
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])

        return sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))

    def trap(self, height):
        # 非常的巧妙

        n = len(height)
        left = 0  # 左指针只向右移动
        right = n-1  # 右指针只向左移动
        leftMax = 0
        rightMax = 0
        area = 0
        while left < right:
            leftMax = max(height[left], leftMax)
            rightMax = max(height[right], rightMax)
            if height[left] < height[right]:
                area += leftMax - height[left]
                left += 1
            else:
                area += rightMax - height[right]
                right -= 1
        return area


if __name__ == "__main__":
    s = Solution()

    height = [4, 2, 0, 3, 2, 5]
    # height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(s.trap(height))
