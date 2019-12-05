class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #n<4的时候先手必胜，n==4时，先手必负，5=<n<=7时，先手必胜，n==8时后手必胜
        #所以return n%4>0
        return n%4>0
            
        

if __name__ == '__main__':
    n=5
    print(Solution().canWinNim(n))
