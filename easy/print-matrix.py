# encoding:utf-8
"""
问题描述：顺时针打印矩阵
解决方案：每次输出矩阵的第一行，然后把剩下的部分进行逆时针90度翻转
"""

class Solution(object):
    def printMatrix(self, matrix):
        res = []
        while len(matrix)>1:
            res.extend(matrix[0])
            matrix = matrix[1:]
            matrix = self.turnMatrix(matrix)

        res.extend(matrix[0])
        print(res)
    def turnMatrix(self, matrix):
        # 逆时针旋转90度，将当前的坐标的行列坐标换位置，且把之前的列坐标逆序放到行坐标
        m = len(matrix)
        n = len(matrix[0])
        new_matrix = [[0]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                new_matrix[i][j] = matrix[j][n-i-1]
        return new_matrix



if __name__ == "__main__":
    matrix =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    s = Solution()
    s.printMatrix(matrix)
    
