# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 4:09 下午
# @Author  : Mohn
# @FileName: 4-median-of-two-sorted-arrays.py


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        n_max = max(m, n)
        n_mid = (m+n)//2
        if m == 0:
            return (nums2[n_mid]+nums2[n_mid-1])/2 if not n % 2 else nums2[n_mid]
        if n == 0:
            return (nums1[n_mid]+nums1[n_mid - 1])/2 if not m % 2 else nums1[n_mid]
        res = []
        i = 0
        j = 0
        num = 0
        while n_max+2:

            if i+j == n_mid or i+j == n_mid+1:
               res.append(num)
            if len(res) == 2:
                break
            if i >= m and j >= n:
                break
            elif i >= m and j < n:
                num = nums2[j]
                j+=1
            elif i < m and j >= n:
                num = nums1[i]
                i+=1
            else:
                if nums1[i] > nums2[j]:
                    num=nums2[j]
                    j+=1
                else:
                    num=nums1[i]
                    i+=1
            n_max -= 1
        if (m+n) % 2 ==0 :
            return sum(res)/2
        else:
            return res[-1]


if __name__ == "__main__":
    s = Solution()
    nums1 = [2, 3, 4, 5]
    nums2 = [1]
    print(s.findMedianSortedArrays(nums1, nums2))