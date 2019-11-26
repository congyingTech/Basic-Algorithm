class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        print([ [1-i for i in row[::-1]] for row in A ])
            


if __name__ == "__main__":
    s = Solution()
    A = [[1,1,0],[1,0,1],[0,0,0]]
    s.flipAndInvertImage(A)