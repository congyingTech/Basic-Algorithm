# encoding:utf-8
"""
问题描述：
求解nums的全排列
解决方案：
回溯法
"""


class Solution(object):
    def isSafe(self, i, pos, record, n):
        if record[i]==False and pos < n:
            return True
        return False

    def permute_util(self, nums, pos, record, res, temp, n):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """ 
        if pos == n and temp not in res:
            res.append(temp[:])
            return

        for i in range(n):
            if self.isSafe(i, pos, record, n):
                temp.append(nums[i])
                record[i] = True
                self.permute_util(nums, pos+1, record, res, temp, n)
                record[i] = False
                temp.pop()

    def permute(self, nums):
        res = []
        temp = []
        n = len(nums)
        record = [False]*n
        pos = 0
        self.permute_util(nums, pos, record, res, temp, n)
        return res
            


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3]
    print(s.permute(nums))