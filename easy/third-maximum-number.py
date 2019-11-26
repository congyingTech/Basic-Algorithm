class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if len(nums)<3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4,5,6]
    a = s.thirdMax(nums)
    print(a)