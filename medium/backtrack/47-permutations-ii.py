"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii

和46的区别是47可以包含重复的字母
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(pos=0):
            # 终止条件
            if pos == n and nums[:] not in res:
                res.append(nums[:])
                return
            for index in range(pos, n):
                # 修改路径，nums分为左右两部分，动态维护
                nums[pos], nums[index] = nums[index], nums[pos]
                # 回溯
                backtrack(pos + 1)
                # 退回到原来的状态
                nums[pos], nums[index] = nums[index], nums[pos]

        n = len(nums)
        backtrack()
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, 5, 1]
    print(s.permute(nums))
