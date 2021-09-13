# -*- coding: utf-8 -*-
# @Time    : 2021/9/13 3:48 下午
# @Author  : Mohn
# @FileName: 394-decode-string.py
"""
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
"""

# class Solution:
#     def decodeString(self, s: str) -> str:
#         stack = []
#         for i in s:
#             if i == ']':
#                 strs = ''
#                 repeat = ''
#                 while stack[-1] != '[':
#                     strs = stack.pop() + strs
#                 stack.pop()
#                 while stack and stack[-1].isdigit():
#                     repeat = stack.pop() + repeat
#                 stack.append(int(repeat) * strs)
#                 continue
#             stack.append(i)
#         return ''.join(stack)


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        sta = []
        for i in s:
            if i != ']':
                sta.append(i)
            else:
                sta_str = ''
                while sta[-1] != '[':
                    sta_str = sta.pop() + sta_str
                sta.pop()
                sta_str_num = ''
                while sta and sta[-1].isdigit():
                    sta_str_num = sta.pop() + sta_str_num
                str_num = int(sta_str_num)
                res = ''
                while str_num > 0:
                    res += sta_str
                    str_num -= 1
                sta.append(res)
        return "".join(sta)


if __name__ == "__main__":
    s = Solution()
    sr = "3[a]2[bc]"
    sr = "2[abc]3[cd]ef"
    sr = "3[a2[c]]"
    sr = "100[leetcode]"
    sr = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    print(s.decodeString(sr))


