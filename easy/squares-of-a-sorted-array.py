#coding:utf-8
class Solution(object):
    def sortedSquares(self, A):
        """
        i是负数部分的指针，j是正数部分的指针
        :type A: List[int]
        :rtype: List[int]
        """
        N = len(A)
        j = 0
        res = []
        while j < N and A[j]<0:
            j += 1
        i = j - 1
        while i>=0 and j<N:
            if A[i]**2 < A[j]**2:
                res.append(A[i]**2)
                i -= 1
            else:
                res.append(A[j]**2)
                j += 1            
        while i>=0:
            res.append(A[i]**2)
            i-=1
        while j<N:
            res.append(A[j]**2)
            j+=1
        return res

if __name__ == "__main__":
    s = Solution()
    A = [-10, -7, -3, -1, 4, 5, 8]
    s.sortedSquares(A)