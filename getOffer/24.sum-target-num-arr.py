# encoding:utf-8
"""
问题描述：
问题1:递增的有序数组，求和为target的两个元素。
问题2:输入一个正数s，打印出所有和为s的连续正数序列，例如输入15，可以和为15的有1+2+3+4+5 = 4+5+6 = 7+8
解决方案：
1）递增的数组，可以设定两个指针，头指针和尾指针，然后头尾加和
2）问题2的解决方案参考了问题1，同样可以定义两个指针small和big，当small和big区间内的元素的和大于target的时候，就把small向前移动，直到等于target
如果小于target的时候就向前移动big，直到等于target。
"""
class Solution(object):
    def findSumEqualTarget(self, arr, target):
        p1 = 0
        p2 = len(arr) - 1
        while p1!=p2:
            if arr[p1]+arr[p2] == target:
                return [arr[p1], arr[p2]]
            elif arr[p1] + arr[p2] < target:
                p1 += 1
            else:
                p2-=1

class Solution1(object):
    def findSumEqualTarget(self, target):
        small_min, big_max = 1, (target+1)//2
        small ,big = 1, 2
        while small >= small_min and small < big_max and big <= big_max:
            cursum = sum([i for i in range(small, big+1)])
            if cursum < target:
                big += 1
            elif cursum > target:
                small += 1
            else:
                print([i for i in range(small, big+1)])
                big += 1        

if __name__ == "__main__":
    s = Solution()
    arr = [1,2,4,7,11,15]
    target = 15
    res = s.findSumEqualTarget(arr, target)
    print(res)

    s1 = Solution1()
    s1.findSumEqualTarget(target)