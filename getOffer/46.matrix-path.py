# encoding:utf-8
"""
问题描述：
设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中任意一格开始，
每一步可以在矩阵中向左，右，上，下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不可能再次进入该格子。
例如，matrix=
[a b c e
 s f c s
 a d e e 
]，包含一条bcced的路径。
解决方案：
经典的回溯法解决的问题。可以求解出path的首端到末端的所有paths，看指定的path是否存在paths中
"""

class Solution(object):

    def solveFindFath(self, matrix, rows, cols, paths, i, j):
        if not paths:
            return True
        # 遍历过i，j位置的元素置为空，避免二次遍历到
        matrix[i][j] = ''
        # 处于i，j位置上时，可以左右上下移动四个选项
        # 向下走
        if i+1<rows and matrix[i+1][j] == paths[0]:
            return self.solveFindFath(matrix, rows, cols, paths[1:], i+1, j)
        # 向上走
        elif i-1>=0 and matrix[i-1][j] == paths[0]:
            return self.solveFindFath(matrix, rows, cols, paths[1:], i-1, j)
        # 向左走
        elif j-1>=0 and matrix[i][j-1] == paths[0]:
            return self.solveFindFath(matrix, rows, cols, paths[1:], i, j-1)
        # 向右走
        elif j+1<cols and matrix[i][j+1] == paths[0]:
            return self.solveFindFath(matrix, rows, cols, paths[1:], i, j+1)
        else:
            return False

    def findPathInMatrix(self, matrix, rows, cols, path):
        for i in range(rows):
            for j in range(cols):
                # 找到入口的位置
                if matrix[i][j] == path[0]:
                    if self.solveFindFath(matrix, rows, cols, path[1:], i, j):
                        return True
        return False



if __name__ == '__main__':
    matrix = [['a','b','c','e'],
              ['s', 'f', 'c', 's'],
              ['a', 'd', 'e', 'e']
             ]
    path = 'bcfed'
    s = Solution()
    print(s.findPathInMatrix(matrix, 3,4,path))