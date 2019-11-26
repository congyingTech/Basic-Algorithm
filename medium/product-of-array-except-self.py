# encoding:utf-8
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L = [1]
        R = [1]
        for i in range(1, len(nums)):
            L.append(nums[i-1]*L[i-1])
        for i in range(len(nums)-1, 0, -1):
            R.append(nums[i]*R[len(nums)-i-1])
        for i in range(len(nums)):
            L[i] = L[i]*R[len(nums)-i-1]
        return L
        
if __name__ == "__main__":
    s = Solution()
    nums = [4, 5, 1, 8, 2]
    #output = [24,]
    print(s.productExceptSelf(nums))