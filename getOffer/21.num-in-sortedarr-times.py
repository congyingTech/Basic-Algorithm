# encoding:utf-8
"""
题目描述：
统计一个数字k在排序数组中出现的次数，例如输入[1,2,3,3,3,3,4,5]和数字3，3出现了4次所以输出4。
解决方案：
1）暴力法，O(n)
2）二分查找算法(因为数组是排序的自然而然的想到),O(logn)，非常的巧妙
用二叉查找第一个k
"""
class Solution(object):
    def findCount(self, arr, k):

        firstK = self.getFirstK(arr, 0, len(arr)-1, k)
        lastK = self.getLastK(arr, 0, len(arr)-1, k)
        print(lastK-firstK+1) 

    def getFirstK(self, arr, start, end, k):
        if start == end:
            return
        mid = (end+start) // 2
        if arr[mid] < k:
            firstK = self.getFirstK(arr, mid+1, end, k)
        elif arr[mid] > k:
            firstK = self.getFirstK(arr, start, mid, k)
        else:
            if arr[mid-1] == k:
                firstK = self.getFirstK(arr, start, mid, k)
            else:
                firstK = mid
    
        return firstK

    def getLastK(self, arr, start, end, k):
        if start == end:
            return 
        mid = (end+start) // 2
        if arr[mid] < k:
            lastK = self.getLastK(arr, mid+1, end, k)
        elif arr[mid] > k:
            lastK = self.getLastK(arr, start, mid, k)
        else:
            if arr[mid+1] == k:
                lastK = self.getLastK(arr, mid+1, end, k)
            else:
                lastK = mid
        return lastK        

if __name__ == "__main__":
    s = Solution()
    arr = [1,2,3,3,3,3,3,4,4,5,5,10]
    k = 10
    s.findCount(arr, k)