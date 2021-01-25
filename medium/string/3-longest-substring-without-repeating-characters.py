#https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""
找出最长不重复字符串的长度

解题思路：
举例：abccdfee
从第一个字符开始
(a)bccdfee，a为首的字符串，abc是最长不重复
a(b)ccdfee，b为首的字符串，bc是最长不重复
ab(c)cdfee，c为首的字符串，c是最长不重复

"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        pass


if __name__ == "__main__":
    s = Solution()
    a = 'abccdba'
    s.lengthOfLongestSubstring(a)
