# encoding:utf-8
"""
问题描述：
求A和B的最长公共子序列
解决方案：
动态规划，假设L(m,n)是m长度的A和n长度的B的最长的公共子序列，
如果A[m]==B[n]，那么L(m,n) = L(m-1, n-1) + 1, 
如果A[m]!=B[n]，那么L(m,n) = max(L(m-1, n), L(m, n-1))
"""
class Solution(object):
    def findLCSLength1(self, A, B):
        # 递归的方法
        m = len(A)
        n = len(B)
        if m == 0 or n == 0:
            return 0
        elif A[m-1] == B[n-1]:
            return self.findLCSLength1(A[:m-1], B[:n-1])+1
        else:
            return max(self.findLCSLength1(A[:m-1], B[:n]), self.findLCSLength1(A[:m],B[:n-1]))

    def findLCSLength(self, A, B):
        # 制表法
        m = len(A)
        n = len(B)
        
        # res[0][0]表示有A中有0个元素，B中有0个元素，res[m][n]表示A中有m个元素和B中有n个元素
        res = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    res[i][j] = 0
                # i,j表示A中有i个元素，B中有j个元素时，这时候在第i个元素在A的坐标是i-1，第j个元素在B中的坐标是j-1
                elif A[i-1] == B[j-1]:
                    res[i][j] = res[i-1][j-1]+1
                else:
                    res[i][j] = max(res[i-1][j], res[i][j-1]) 
        print(res[m][n])

    

if __name__ == "__main__":
    s = Solution()
    A = 'abcdef'
    B = 'bdf'
   # print(s.findLCSLength1(A, B))
    # s.findLCSLength(A,B)
    s.findLCSLength(A,B)