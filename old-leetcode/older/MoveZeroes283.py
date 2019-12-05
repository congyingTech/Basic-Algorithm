class Solution(object):
    def moveZeroes(self, nums):
       
        count = nums.count(0)
        while count:
            for i,e in enumerate(nums):
                if e == 0 and i<len(nums)-1:
                    nums[i] = nums[i+1]
                    nums[i+1] = e
            count -= 1
               

if __name__ == "__main__":
    s = Solution()
    nums = [0,1,0,3,12]
    print(s.moveZeroes(nums))