# encoding:utf-8
"""
问题描述：

解决办法：
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m>0 and n>0:
            if nums1[m-1]<nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
        nums1[:n] = nums2[:n]
        print(nums1)

if __name__ == "__main__":
    s = Solution()
    nums1 = [1,3,5,7,9,0,0,0,0,0,0]
    nums2 = [2,4,6,8,10,12]
    m = 5
    n = 6
    s.merge(nums1, m, nums2, n)