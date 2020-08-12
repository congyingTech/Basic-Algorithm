#encoding:utf-8
"""
问题描述：
寻找最小的k个数
[4,5,1,6,2,7,3,8]
最小[1,2,3,4]
解决方案：
3）快排 O(nlogn)
1）k遍，每遍选出最小值，时间复杂度是O(kn)
2）最大堆
	获取最小的k个数字
	因为heapq只有最小堆，没有最大堆，所以在入堆的时候，存入原始数据的负数。
    在出堆之后，再取出存取的数据的负数。
    :param array: 数组
    :param k: 整数
"""
import heapq

def get_least_numbers_3(array, k):
	
    # 最大堆
    max_heap = []
    # 边界条件
    if not array or k < 1 or k > len(array):
        return
    
    # 遍历数组
    for ele in array:
    	# 当最大堆中元素数量小于k时，直接插入元素到堆中。
        if len(max_heap) < k:
            heapq.heappush(max_heap, -ele) # push元素到堆中
        else:
        	# 堆中的最小值
            max_value = -heapq.heappushpop(max_heap) # pop最小元素出堆, 然后取负数
            if ele < max_value:
            	heapq.heappush(max_heap, -ele) # push元素到堆中

    return map(lambda x:-x, max_heap)

class Solution(object):
    
    def getMinKnums(self, nums, k):
        """
        快排的方法
        """
        nums, pivot_index = self.partition(0, len(nums), nums)
        if pivot_index==k:
            return nums[:k]
        mid = ()
        while k != mid:
            # if k>
            pass
            
        
        
    def partition(self, start, end, nums):
        pivot = nums[start]
        i, j = start, end
        while i!=j:
            while i<j and nums[i]<=pivot:
                i+=1
            while i<j and nums[j]>=pivot:
                j-=1
            if i < j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
        nums[start] = nums[i]
        nums[i] = pivot
        return nums, i
         

    def getMinKnums1(self, nums, k):
        """
        堆的方法
        """
        pass




if __name__ == "__main__":
    array = [4,5,1,6,2,7,3,8]
    k = 4
    print(get_least_numbers_3(array, k))