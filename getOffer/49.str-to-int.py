# encoding:utf-8
"""
问题描述：
把字符串转换成整数
解决方案：
字符0的ascii码是48，那么让所有字符减去48就是字符代表的int的值
"""
class Solution(object):
    def strToInt(self, s):
        res,mult,flag = 0,1,1
        if not s:
            return res
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                flag = -1
            s = s[1:]
        for i in range(len(s)-1, -1, -1):
            if '9' >= s[i] >= '0':
                res += (ord(s[i]) - 48)*mult
                mult = mult * 10
            else:
                return 0
        return res*flag


if __name__ == "__main__":
    s = Solution()
    string = '-2200'
    print(s.strToInt(string))