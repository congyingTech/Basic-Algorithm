# encoding:utf-8
"""
问题描述：找出最少需要增加的括号，使括号字符串变得有效。
exp："())" 最左增加一个"(" 就可以有效，所以是1
"()))((" 最左增加两个”((“，最右增加两个"))"

解决办法：
"""

class Solution(object):
    def minAddToMakeValid(self, S):
        """
        解法1:利用）不能再匹配成功的原理，用bal计数balance当前的结果。
        比较技巧性的解法，bal维持一个balance，一直在-1，0，n之间浮动
        symobol = '('则+1，=')'则-1，
        bal=0，代表目前凑对成功，
        bal=-1代表目前剩余一个')'，此时就ans+=1，把这个多余的')'计数到最后结果，因为）不可能再匹配成功了，且bal+=1置为0
        bal=n，代表剩余n个'('，还有希望匹配成功。
        """
        ans = bal = 0
        for symbol in S:
            bal += 1 if symbol == '(' else -1
            # It is guaranteed bal >= -1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal

    def minAddToMakeValid1(self, S):
        """
        比较简单理解的方法
        """
        while "()" in S:
            S = S.replace("()", "")
        
        return len(S)

if __name__ == "__main__":
    s = Solution()
    S = ")()((()()))))))"
    s.minAddToMakeValid(S)
