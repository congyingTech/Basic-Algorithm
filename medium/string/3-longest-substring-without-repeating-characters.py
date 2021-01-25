#https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""
找出最长不重复字符串的长度

解题思路：
以 (a)bcabcbb 开始的最长字符串为 (abc)abcbb；
以 a(b)cabcbb 开始的最长字符串为 a(bca)bcbb；
以 ab(c)abcbb 开始的最长字符串为 ab(cab)cbb；
以 abc(a)bcbb 开始的最长字符串为 abc(abc)bb；
以 abca(b)cbb 开始的最长字符串为 abca(bc)bb；
以 abcab(c)bb 开始的最长字符串为 abcab(cb)b；
以 abcabc(b)b 开始的最长字符串为 abcabc(b)b；
以 abcabcb(b) 开始的最长字符串为 abcabcb(b)。
发现，不重复子串的结束的位置也是递增的，这一点是因为子串不重复，所以不用每一次都从子串的头部开始遍历比较，只需基于上次的子串停止的位置进行操作就行。

双指针，左指针放在不重复字符串最左端，右指针放在不重复字符串最右端
一个set记录不重复字符串，
左指针每次都向右边移动一步，左指针向右移动时，set remove当前指针所指向的字符
右指针每次判断是否有重复和是否超长而向右移动，右指针向右移动时，set add指针所指向的字符

"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        temp = set()
        n = len(s)
        j = -1  # j从-1开始，因为两个指针都要从0开始走
        res = 0
        for i in range(n):
            if i != 0:
                temp.remove(s[i-1])
            while j+1 < n and s[j+1] not in temp:
                temp.add(s[j+1])
                j += 1
            res = max(res, j-i+1)
        return res


if __name__ == "__main__":
    s = Solution()
    a = 'abcabcbb'
    s.lengthOfLongestSubstring(a)
