"""
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

 

示例 1：

输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
 

提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii

相较于78，输入的数据集是有重复元素的。

"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(pos, temp):
            if temp[:] not in res:
                res.append(temp[:])
            for index in range(pos, n):
                temp.append(nums[index])
                backtrack(index+1, temp)
                temp.pop()
        n = len(nums)
        nums = sorted(nums)
        backtrack(0, [])
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [3, 2, 5, 2]
    res = s.subsetsWithDup(nums)
    print(res)
