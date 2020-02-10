# encoding:utf-8
"""
问题描述：
求数组里面的逆序对的总数
比如[7,5,6,4]的逆序对是(7,5),(7,6),(7,4),(6,4),(5,4)
解决方案：
1）直接暴力法：双重循环，时间复杂度O(n^2)
2）用归并排序的思想：归并的优点在于，时间复杂度是O(nlogn)，且归并排序是稳定的排序，相对位置变化不大。缺点是需要O(n)的辅助空间
"""
class Solution(object):
    def findReversePair(self, arr, start, end, temp):
        if start == end:
            return 0

        mid_index = (start+end)//2  # 这个地方需要格外的小心，因为要保证左右子序列的相对位置
        left_count = self.findReversePair(arr, start, mid_index, temp)
        right_count = self.findReversePair(arr, mid_index+1, end, temp)
        count =  0
        # p1, p2, p3分别是左子序列，右子序列，temp的index。
        # 这里是从后往前比较，原因在于寻找逆序对，左子序列和右子序列分别是有序的，如果左子序列的最后一个值比右子序列的最后一个值大，那么逆序对的长度就是右子序列的长度
        p1, p2, p3 = mid_index, end, end
        
        # merge的过程, 统计数量并进行归并排序
        while p1>=start and  p2>mid_index:
            if arr[p1]>arr[p2]:
                count += p2-mid_index
                temp[p3] = arr[p1]
                p1 -= 1
            else:
                temp[p3] = arr[p2]
                p2-=1
            p3 -= 1 
        #   如果此时有p1或者p2没有遍历完，直接加入到temp中
        while p1>=start:
            temp[p3] = arr[p1]
            p1-=1
            p3-=1
        while p2>mid_index:
            temp[p3] = arr[p2]
            p2-=1
            p3-=1

        # temp是已经排好序的子序列，将其复制给原始数组，这样原始数组可以进行新的归并
        s = start
        while s<=end:
            arr[s] = temp[s]
            s += 1
        return left_count+right_count+count


if __name__ == "__main__":
    s = Solution()
    arr = [7,5,6,4,8,3]
    start =0
    end = len(arr)-1
    temp = [0]*len(arr)
    count = s.findReversePair(arr, start, end, temp)
    print(temp)
    print(count)
    # print(count)
    # print(temp)