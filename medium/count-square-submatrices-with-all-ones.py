#encoding:utf-8
"""
问题描述：
统计每一个元素都为1的方阵的个数
比如
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
边长为1的方阵且元素都为1的方阵的个数是10个
同理2的有4个
3的有一个，
所以总共有15个
解决方案：
"""
class Solution(object):
    def countSquares(self, A):
        for i in range(1, len(A)):
            for j in range(1, len(A[0])):
                A[i][j] *= min(A[i - 1][j], A[i][j - 1], A[i - 1][j - 1]) + 1
        return sum(map(sum, A))

    def countSquares1(self, A):
        m = len(A)
        n = len(A[0])
        

if __name__ == "__main__":
    s = Solution()
    matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
    s.countSquares(matrix)