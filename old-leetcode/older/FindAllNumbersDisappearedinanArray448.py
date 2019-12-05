class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #下面的超时了，但是加入N = set(nums) if i not in N:就不超时了。。。。无语吧
#         result = []
#         lenth = len(nums)
#         for i in range(1,lenth+1):
#             if i not in nums:
#                 result.append(i)
        

        #正负号标记法，abs(n)-1是下标值
        #nums[abs(n)-1]是取出nums的对应下标值，相同两个元素的下标值相同，所以如果有重复的元素，必然有没有
        #变成负数的下标值，最后找出不是负数的下标+1即可
        for n in nums:
            nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
        
        print (nums)
        return [i + 1 for i, n in enumerate(nums) if n > 0]


if __name__ == "__main__":
    s = Solution()
    nums = [4,3,2,7,8,2,3,1]
    print(s.findDisappearedNumbers(nums))
