# encoding:utf-8
"""
问题描述：
Input: [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]
这个题目的意思是找到一个序列使得 打开一张牌然后把下一张牌挪到牌堆最下，保证打开牌的顺序是递增的。
打开2，挪动13: 3, 11, 5, 17, 7, 13 
打开3，挪动11: 5, 17, 7, 13, 11
打开5，挪动17: 7, 13, 11, 17
打开7，挪动13: 11, 17, 13
打开11，挪动17: 13, 17
打开13，挪动17: 17
打开17.
所以打开牌的顺序就是2,3,5,7,11,13,17是有序的，所以[2,13,3,11,5,17,7]是符合要求的。
解决方案：
每次可以用index模拟reveal和remove的操作
[17,13,11,2,3,5,7]
[2,3,5,7,11,13,17]
"""
class Solution:
    def deckRevealedIncreasing(self, deck):
        ref, res, ind = sorted(deck, reverse = True), deck[:], list(range(len(deck)))
        while ref:
            # reveal top item，reveal的值是从小到大的
            res[ind[0]] = ref.pop()
            # + ind[1]是把下一个元素挪动到队尾
            ind = ind[2:] + [ind[1]] if len(ind) > 1 else []
        return res    

if __name__ == "__main__":
    s = Solution()
    deck = [17,13,11,2,3,5,7]
    s.deckRevealedIncreasing(deck)

