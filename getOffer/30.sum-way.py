# encoding:utf-8
"""
问题描述：
写一个函数求两个正数的和，要求在函数体内不得使用+、-、*、/四则运算符号。
解决方案：
1)异或的方法可以得到不带进位的加和，比如1000^1010 = 0010; 
位与可以得到a，b都为1的位数，只有该位输出为1，把结果左移一位就是进位；
然后把异或的结果和位与的进位的结果像上面一样进行两部操作，直到没有进位。
"""

class Solution(object):
    def getSum(self, a, b):
        temp=0
        while b:
            temp = a^b
            b = (a&b)<<1  # b在这里是进位
            a = temp  # a在这里是两者的异或结果
        print(a)
        
if __name__ == "__main__":
    s = Solution()
    a = 10
    b = 119
    s.getSum(a, b)