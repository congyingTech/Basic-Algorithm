# encoding:utf-8
"""
问题描述：
从扑克牌中随机抽取5张牌，判断是不是一个顺子，2～10是数字本身，A是1，J～K是11，12，13，大小王是任意的数字。
解决方案：
将抽到的牌进行排序，首先有两个一样的数字的数组不可能出现顺子了，其次，看数组中0的数量，如果0的数量等于数与数之间间隙的大小，那么也是顺子。
(比较简单，不浪费时间了。。。)
"""

class Solution(object):
    def isContinuous(self, random_deck):
        pass

if __name__ == "__main__":
    s = Solution()
    random_deck = [2,3,1,0,4]
    s.isContinuous(random_deck)