class Solution(object):
    def arrayPairSum(self, nums):
        new_nums = sorted(nums)
        return sum(new_nums[::2])

if __name__ =='__main__':
    nums = [2,5,4,8]
    s = Solution()
    print(s.arrayPairSum(nums))