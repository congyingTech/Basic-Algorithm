# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 7:44 下午
# @Author  : Mohn
# @FileName: 215-kth-largest-element-in-an-array.py
"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

 

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findKthLargest(self, nums, k):
        # write code here
        left = 0
        right = len(nums) - 1
        self.quickSort(nums, left, right)
        return nums[-k]

    def quickSort(self, a, left, right):
        if left > right:
            return
        pivot = a[left]
        i, j = left, right
        while i != j:
            while i < j and a[j] >= pivot:
                j -= 1
            while i < j and a[i] <= pivot:
                i += 1
            if i < j:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp

        a[left] = a[i]
        a[i] = pivot
        self.quickSort(a, left, i - 1)
        self.quickSort(a, i + 1, right)


if __name__ == "__main__":

    print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
