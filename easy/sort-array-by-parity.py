# coding:utf-8
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A.sort(key=lambda k:k%2)
        return A

    def sortArrayByParity1(self, A):
        current = 0 # 用于记录奇数所在的位置
        for i, a in enumerate(A):
            if a%2 == 0: # 如果a是偶数，和奇数交换位置，因为偶数要放在前面
                A[current], A[i] = A[i], A[current] # 标准的交换两个元素的python语句
                current = current + 1
        return A

if __name__ == "__main__":
    s = Solution()
    A = [2,1,3,4]
    #a = s.sortArrayByParity(A)
    b = s.sortArrayByParity1(A)
    #print(a)
    print(b)