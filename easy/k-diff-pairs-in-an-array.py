import collections
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = []
        for i,n in enumerate(nums):
           
            new_nums = nums[0:i]
            new_nums.extend(nums[i+1:])
            for j in new_nums:
                diff = abs(n-j)
                if diff == k :
                    r = sorted([n,j])
                    if r not in res:
                        res.append(r) 
        print(res)
        return len(res)
    
    def findPairs2(self, nums, k):
        nums_s = set(nums)
        if k>0:
            nums_k = set([num+k for num in nums])
            return len(nums_k&nums_s)
        elif k == 0:
            return len([v for v in collections.Counter(nums).values() if v > 1])
        else:
            return 0

if __name__ == "__main__":
    s = Solution()
    res = s.findPairs([1,3,1,5,4], 0)
    print(res)