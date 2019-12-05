# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
#-*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        lists = []
        result = 1
        if number == 0:
            return 0
        if number == 1:
            return result
        lists.append(result)
        lists.append(result)
        i = 2
        while i <= number:
            lists.append(lists[i - 1] + lists[i - 2])
            i += 1
        return lists[i - 1]