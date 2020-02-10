# encoding:utf-8
"""
问题描述：
在一个长度为n的数组里所有的数字都在0～n-1的范围内。数组中有数字是重复的，但不知道是哪些，所以找出所有的重复数字以及重复的次数。
解决方案：
1）直觉上用一个dict记录出现过的数字，并统计次数。时间空间复杂度都是O(N)
2）因为数组中数字的大小都在0～n-1范围内，所以可以通过遍历数组的下标，如果当前的下标和对应的数字是一样的，则遍历下一个；
否则指向i坐标对应的数字m对应的坐标，看arr[i]和arr[m]是否相等，如果相等的话，那么打印重复的数字，如果不相等，就把第m个数字
和第i个数字交换，把当前的数字m放到它应该在的位置上。
"""
class Solution(object):
    def findRepeatNum(self, arr):
        for i in range(len(arr)):
            if arr[i] == i:
                continue
            while arr[i]!=i:
                m = arr[i]
                temp = arr[m]
                if m == temp:
                    print(m)
                    break
                arr[i] = temp
                arr[m] = m

if __name__ == "__main__":
    s = Solution()
    arr = [2,3,1,0,2,5,3]
    s.findRepeatNum(arr)