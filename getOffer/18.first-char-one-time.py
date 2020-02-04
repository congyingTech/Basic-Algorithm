# encoding:utf-8
"""
问题描述：寻找第一个只出现一次的字符
例如abaccdeff 输出的是b
解决方案：
1)最直白的就是统计出现的次数，遍历一遍用map记录每个字符出现的次数，然后把出现一次的找出来，index位置，把位置小的那个字符输出
1）居然还是时间复杂度最低的。。。更差的是双重循环
"""
class Solution(object):
    def findFirstCharOnetime(self, arr):
        char_count_dict = dict()
        for char in arr:
            if char not in char_count_dict:
                char_count_dict[char] = 1
            else:
                char_count_dict[char] += 1
        print(char_count_dict)

        for char in arr:
            if char_count_dict.get(char)==1:
                print(char)
                break

if __name__ == "__main__":
    s = Solution()
    arr = 'abaccdeff'
    s.findFirstCharOnetime(arr)