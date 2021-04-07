"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations

思路：典型的回溯法解题思路

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
            if pos == n:
                res.append(nums[:])
                return
            for index in range(pos, n):
                # nums分为左右两部分，动态维护
                nums[pos], nums[index] = nums[index], nums[pos]
                backtrack(pos + 1)
                # 回溯
                nums[pos], nums[index] = nums[index], nums[pos]

        n = len(nums)
        backtrack()
        return res


class Solution1(object):
    def permute(self, nums):
        res = []
        n = len(nums)
        # 用来记录元素是否被使用过，十分关键
        used = [False for _ in range(n)]

        def backtrack(pos, temp):
            if len(temp[:]) == n:
                res.append(temp[:])
                return
            for index in range(0, n):
                if not used[index]:
                    temp.append(nums[index])
                    used[index] = True
                    backtrack(pos+1, temp[:])
                    temp.pop()
                    used[index] = False
                else:
                    continue

        backtrack(0, [])
        return res


if __name__ == "__main__":
    s = Solution1()
    nums = ['A', 'B', 'C']
    print(s.permute(nums))
