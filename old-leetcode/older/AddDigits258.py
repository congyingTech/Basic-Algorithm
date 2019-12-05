class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        n_s = str(num)
        lenth = len(n_s)
        if lenth < 2:
            return num
        num = 0 
        for i in range(lenth):
            num += int(n_s[i])
        return self.addDigits(num)
if __name__ == '__main__':
    s = Solution()
    num = 13243214
    print(s.addDigits(num))