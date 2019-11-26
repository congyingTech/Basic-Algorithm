class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res =""
        for char in str:
            if ord(char) >=65 and ord(char) <= 90:
                res +=chr(ord(char)+32)
            else:
                res+=char
        
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.toLowerCase('ABABABA')
    print(res)
