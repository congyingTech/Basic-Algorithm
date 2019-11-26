class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A_set_sum = sum(set(A))
        diff = sum(A) - A_set_sum
        return diff / (len(A)/2 -1)
            

if __name__ == "__main__":
    s = Solution()
    A = [7,2,3,4,5,6,1,7,7,7,7,7]
    res = s.repeatedNTimes(A)
    print(res)