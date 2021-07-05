# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 5:32 下午
# @Author  : Mohn
# @FileName: 20-valid-parentheses.py

"""
有效的括号
[],{},()算是有效的括号匹配
栈匹配,栈里记录左括号，然后出现右括号的时候，出栈匹配
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sta = list()
        for symbol in s:
            if symbol in ['{', '(', '[']:
                sta.append(symbol)
            else:
                if not sta:
                    return False
                if symbol == ']':
                    match = '['
                elif symbol == '}':
                    match = '{'
                else:
                    match = '('
                c = sta.pop()
                if c != match:
                    return False
        if len(sta)!=0:
            return False
        return True


if __name__ == "__main__":
    so = Solution()
    s = "()"
    print(so.isValid(s))
