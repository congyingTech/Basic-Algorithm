# -*- coding: utf-8 -*-
# @Time    : 2021/10/26 11:35 上午
# @Author  : Mohn
# @FileName: 49-group-anagrams.py

"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母都恰好只用一次。

 

示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
思路：异位词指的是组成单词的元素相同，但是不同的顺序组成了不同的词组

"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = dict()
        for st in strs:
            st_s = ''.join(sorted(st))
            if not map.get(st_s, None):
                temp = []
            else:
                temp = map[st_s]
            temp.append(st)
            map[st_s] = temp
        return list(map.values())


if __name__ == "__main__":
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.groupAnagrams(strs))
