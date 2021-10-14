# -*- coding: utf-8 -*-
# @Time    : 2021/6/22 5:45 下午
# @Author  : Mohn
# @FileName: 17-letter-combinations-of-a-phone-number.py
"""
解题思路：回溯法
类似于77组合问题，组合问题是自己跟自己组合的方案有多少种，这个是自己和别人组合的方案有哪些。
不同在于自己和自己的组合，backtrack不用从自己算起，而自己和别人组合，都要从第一个算起，backtrack(index+1)
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                     "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if not digits:
            return []

        def backtrack(index):
            if index == len(digits):
                res.append(''.join(combination))
            else:
                for letter in digit_map.get(digits[index]):
                    combination.append(letter)
                    backtrack(index+1)
                    combination.pop()
            return res

        combination = list()
        res = list()
        backtrack(0)
        return res


if __name__ == "__main__":
    s = Solution()
    # digits的长度0-4
    digits = "9264"
    print(s.letterCombinations(digits))