# encoding:utf-8
"""
问题描述：
给定一个数组A[0,n-1], 请构建一个数组B[i] = A[0]*...A[i-1]*A[i+1]*...*A[n-1]
期间不能用除法
解决方案：
1)简单粗暴：直接双重循环求乘积
2）把B[i]= A[0]*...A[i-1]*A[i+1]*...*A[n-1]分成两部分
A[0]*....A[i-1]从前往后遍历相乘
和A[i+1]*....A[n-1]从后往前遍历相乘
"""

class Solution(object):
    def buildMultMatrix(self, arr):
        n = len(arr)
        B = [None]*n
        B[0] = 1
        for i in range(1, n):
            B[i] = B[i-1]*arr[i-1]
        temp = 1
        for i in range(n-2, -1, -1):
            temp *= arr[i+1]
            B[i] *= temp
        return B

if __name__ == "__main__":
    s = Solution()
    arr = [1,2,3,4,5,6,7,8]
    s.buildMultMatrix(arr)