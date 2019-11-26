#encoding:utf-8
# Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
# Output: 29

class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        wrong--局部最优，要找的是两个子序列的和最优
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        if len(A)<=0 :
            return 0
        ans_max_L = 0
        res_L = {}
        ans_max_M = 0
        for i in range(len(A)-L+1):
            val = sum(A[i:i+L])
            if val>ans_max_L:
                ans_max_L = val
                res_L[val] = i
        index_L = res_L.get(ans_max_L)
        A = A[0:index_L]+A[index_L+L:]

        for j in range(len(A)-M+1):
            val = sum(A[j:j+M])
            if val>ans_max_M:
                ans_max_M = val
        return ans_max_L+ans_max_M
                
    def maxSumTwoNoOverlap1(self, A, L, M):
        """
        use DP 
        step1:find cursum of A
        step2:two case about location of maxL & maxM---
             one possible case is L is before M
             another possible case is M is before L
        """
        # step1: cal cursum
        for i in range(1, len(A)):
            A[i] += A[i-1]
        
        # initial
        res = A[L+M-1]
        Lmax = A[L-1]
        Mmax = A[M-1]
        # case1: |----L----M----|
        for i in range(L+M, len(A)):
            Lmax = max(Lmax, A[i-M]-A[i-M-L])
            res = max(res, Lmax+A[i]-A[i-M])
        print('case1 max res is {}'.format(res))
        # case2: |----M----L----|
        for i in range(L+M, len(A)):
            Mmax = max(Mmax, A[i-L]-A[i-L-M])
            res = max(res, Mmax+A[i]-A[i-L])
        print('case2 max res is {}'.format(res))
        return res

if __name__ == "__main__":
    A = [8,20,20,17,6,3,20,8,12]
    L = 5
    M = 4
    s = Solution()
    print(s.maxSumTwoNoOverlap1(A, L, M))