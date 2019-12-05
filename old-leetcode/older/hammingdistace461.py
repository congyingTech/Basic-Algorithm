class Solution(object):
    def hammingDistance(self, x, y):
        return bin(x^y).count('1')
    
if __name__ == "__main__":
    x=1
    y=4
    s = Solution()
    print(s.hammingDistance(x, y))