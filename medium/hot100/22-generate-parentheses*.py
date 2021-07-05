# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 8:19 下午
# @Author  : Mohn
# @FileName: 22-generate-parentheses*.py
"""
有效括号对数的生成
n=3
()()()
(()())
()(())
(())()
((()))
思路：回溯法

"""


class Solution1:
    def generateParenthesis(self, n):
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans


class Solution(object):
    # 解法超时
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def isValidParenthesis(parenthesis):
            sta = list()
            for paren in parenthesis:
                if paren == '(':
                    sta.append(paren)
                else:
                    if len(sta) == 0:
                        return False
                    c = sta.pop()
                    if c == "(":
                        match = ")"
                    if paren != match:
                        return False
            if sta:
                return False
            return True

        res = []
        ele = ["()" for _ in range(n)]
        ele = ''.join(ele)
        used = [False for _ in range(2*n)]

        def backtrack(pos, temp):
            a = ''.join(temp)
            if len(a) == 2*n and a not in res and isValidParenthesis(a):
                res.append(a)
            for index in range(0, len(ele)):
                if not used[index]:
                    temp.append(ele[index])
                    used[index]=True
                    backtrack(pos+1, temp)
                    temp.pop()
                    used[index]=False

        backtrack(0, [])
        return res


if __name__ == "__main__":
    s = Solution1()
    n = 5
    print(s.generateParenthesis(n))
