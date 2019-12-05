class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        if len(set(nums)) == 1 and nums[0] == 1:
            return len(nums)
        if len(set(nums)) == 1 and nums[0] == 0:
            return 0
        
        indexs = []
        for i, num in enumerate(nums) :
            if num == 0:
                indexs.append(i)
        lenth = len(nums)
        sub = []
        for i, e in enumerate(indexs):
            if i == 0:
                sub.append(e)
            elif i < lenth:
                sub.append(e-indexs[i-1] - 1)
        sub.append(lenth - indexs[-1:][0] - 1)    
        
        return max(sub)
            
        
        

if __name__ == '__main__':
    nums = [0]
    print(Solution().findMaxConsecutiveOnes(nums))
