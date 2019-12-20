# encoding:utf-8
"""
问题描述：
给定一个矩阵，矩阵可以进行任意行和列的0，1转换，转换后的矩阵
每一行都是二进制代码，求矩阵转换后二进制代码最大的和值

解决方案：
优先行转换，将尽量将高位转换为1
其次列转换，每一列的数都是相同的，所以列所在的1，越多越好
"""

class Solution(object):
    def metrixT(self, A):
        m = len(A)
        n = len(A[0])
        columns = [[0]*m for i in range(n)]
        for i, row in enumerate(A):
            for j, col in enumerate(row):
                columns[j][i] = col

        return columns

    def computer_binary_num(self,l):
        n = len(l)
        x = [2**i for i in range(n)]
        l.reverse()
        res = map(lambda a,b:a*b,x,l)
        return sum(res)
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        ## 行：最高位为1
        for ind, row in enumerate(A):
            if row[0] == 0:
                for i,j in enumerate(row):
                    if j == 0:
                        row[i]=1
                    else:
                        row[i]=0
                print(row)
            A[ind] = row

        ## 列：1的数量最多
        # 先进行转置
        A_T = self.metrixT(A)
        for ind, row in enumerate(A_T):
            count0 = 0
            count1 = 0
            for i in row:
                if i == 1:
                    count1+=1
                else:
                    count0+=1
            if count1< count0:
                # 如果1的数目大于0的数目，那么进行转换
               for i,j in enumerate(row):
                    if j == 0:
                        row[i]=1
                    else:
                        row[i]=0 
            A_T[ind] = row
        
        #再进行转置
        A = self.metrixT(A_T)
        res = 0
        for row in A:
            row_sum = self.computer_binary_num(row)
            res += row_sum
        return res        
        

if __name__ == "__main__":
    s = Solution()
    A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    s.matrixScore(A)