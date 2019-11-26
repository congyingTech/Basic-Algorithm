# coding:utf-8
# class Solution(object):
#     def checkPossibility(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         if len(nums)<=2:
#             return True
#         count = 0
#         for index, num in enumerate(nums):
#             if index+1<len(nums):
#                 diff = nums[index+1] - num
#                 if diff < 0:
#                     count += 1
#                     if index-1>=0:
#                         diff_2 = nums[index+1]-nums[index-1]
#                         print(len(nums)-1)
#                         print(index+1)
#                         if (abs(diff_2) <= 0 and index+1!=len(nums)-1) and diff_2<0:
#                             return False

#         if count <= 1:
#             return True
#         else:
#             return False
    
class Solution(object):
    def checkPossibility(self, A):
        """
        for循环是保证了A[i]>A[i+1]的情况只出现一次
        or条件1:p==len(A)-2的意思是，p只要在倒数第二个位置，一定是可以改变的，因为只需要最后一个元素改变
        or条件2:A[p-1]<=A[p+1]保证了p位置的元素在两边的元素一小一大(或者相等)的情况下改变p是可以保证顺序的
        or条件3:A[p]<=A[p+2]保证了p位置和p的下下一个位置一小一大，这样可以通过更改p+1位置的元素保证顺序
        """
        p = None
        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                if p is not None:
                    return False
                p = i
        return (p is None or p == 0 or p == len(A)-2 or
                A[p-1] <= A[p+1] or A[p] <= A[p+2])


if __name__ == "__main__":
    s = Solution()
    nums = [2,3,3,2,4]
    # nums = [1,2,5,3,3]
    # nums = [3,4,2,3]
    res = s.checkPossibility(nums)
    print(res)