class Solution(object):
    #n-1个元素同时加一，相当于另一个元素减一，这样的话相当于，将大于最小值
    #的值减到最小值用的次数
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums)*min(nums)
        
if __name__ == "__main__":
    s = Solution()
    
