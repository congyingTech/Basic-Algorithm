# encoding:utf-8
"""
问题描述：
给定一个非空的数组，求出现k频繁的数
解决方案：
直接的思路是：遍历一遍list，统计list的每个元素出现的频率，然后取top k。时间复杂度是O(n)
可以用heap的思路
"""
from collections import Counter
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)     


if __name__ == "__main__":
    s = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    s.topKFrequent(nums,k)