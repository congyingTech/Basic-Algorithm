class Solution(object):
    def singleNumber(self, nums):
        #考虑异或，相同的数字异或为0，所以将所有的num异或即可
        ans = 0
        for num in nums:
            ans ^= num
        return ans

       
#下面的方法超时        
#         for i in set(nums):
#             if nums.count(i) != 2:
#                 return i
            

if __name__ == '__main__':
    nums = [1,2,5,4,2,5,3,1,4]

    print(Solution().singleNumber(nums))
