# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 2:59 下午
# @Author  : Mohn
# @FileName: meituan.py

class Solution:
    def findKth(self, a, n, K):
        # write code here
        left = 0
        right = n - 1
        self.quickSort(a, left, right)
        return a[-K]

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

if __name__ == '__main__':
    a = [1332802,1177178,1514891,871248,753214,123866,1615405,328656,1540395,968891,1884022,252932,1034406,1455178,821713,486232,860175,1896237,852300,566715,1285209,1845742,883142,259266,520911,1844960,218188,1528217,332380,261485,1111670,16920,1249664,1199799,1959818,1546744,1904944,51047,1176397,190970,48715,349690,673887,1648782,1010556,1165786,937247,986578,798663]
    n = 49
    K = 24
    print(Solution().findKth(a, n, K))



