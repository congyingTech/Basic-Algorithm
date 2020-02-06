# encoding:utf-8
"""
问题描述：
有一组非负的数组，和值为k，求是否存在连续的子序列(长度至少是2)的和值为k或者k的倍数
解决方案：
如果sum(nums[i:j])%k==0且i<j，那么sum(nums[:i])%k == sum(nums[:j])%k, 例如(23 , 2, 4)中, (2+4)%6=0，那么(23+2+4)%6=23%6
有了这个规律就很好求了，g根据玉树相同求出来这么一个i和j 如果j-i>=1那么，返回True。
所以需要一个dict记录sum(nums[:i]) % k，然后在dict中看，如果有相同的余数的元素，就return True


Time complexity: O(n), space complexity: O(min(k, n)) if k != 0, else O(n).
"""

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """    
        if k == 0:
            for i in range(1, len(nums)):
                if nums[i] == nums[i-1]:
                    return True
            return False
        
        dic = {0:-1}
        
        for i in range(len(nums)):
            remainder = sum(nums[:i+1])%k
            if k!=0 and remainder not in dic:
                dic[remainder]=i
            else:
                j = dic[remainder]
                if i-j>=2:
                    return True
        return False

    def checkSubarraySum1(self, nums, k):
        dic = {0:-1}
        summ = 0
        # 这个速度更快，因为统计[:]是非常耗时间的。。。
        for i, n in enumerate(nums):
            if k != 0:
                summ = (summ + n) % k
            else:
                summ += n
            if summ not in dic:
                dic[summ] = i
            else:
                if i - dic[summ] >= 2:
                    return True
        return False

            
            

if __name__ == "__main__":
    s = Solution()
    nums=[0,0]
    k=-1
    print(s.checkSubarraySum1(nums, k))
    