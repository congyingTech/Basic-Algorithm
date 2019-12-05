class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        news = s[::-1]
        for i,e in enumerate(news):
            res += (26**i)*(ord(e)-64)
        return res
if __name__ == "__main__":
    s = Solution()
    a = 'AAA'
    print(s.titleToNumber(a))