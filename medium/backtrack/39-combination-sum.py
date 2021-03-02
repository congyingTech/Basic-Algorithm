"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum

"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(pos, temp):
            if temp[:] not in res and sum(temp[:]) == target:
                res.append(temp[:])

            # 求和，意味着结果可无序
            # 可以重复利用candidates中的元素
            for index in range(pos, n):
                if sum(temp[:]) < target:
                    temp.append(candidates[index])
                    backtrack(index, temp)
                    temp.pop()

        n = len(candidates)
        res = []
        backtrack(0, [])
        print(res)
        return res


if __name__ == "__main__":
    s = Solution()
    candidates = [3, 2, 6, 7]
    target = 7
    s.combinationSum(candidates, target)
