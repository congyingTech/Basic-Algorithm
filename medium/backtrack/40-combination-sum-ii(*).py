"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        超时的解法
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def backtrack(pos, temp):
            if sorted(temp[:]) not in res and sum(sorted(temp[:])) == target:
                res.append(sorted(temp[:]))
                return
            for index in range(pos, n):
                if sum(temp[:]) < target:
                    temp.append(candidates[index])
                    backtrack(index+1, temp)
                    temp.pop()

        res = []
        n = len(candidates)
        backtrack(0, [])
        print(res)
        return res


class Solution2(object):
    def combinationSum2(self, candidates, target):
        """
        改进的版本
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        import collections
        # 为了避免重复，多出了freq的数组

        def backtrack(pos, rest):
            nonlocal sequence
            if sequence[:] not in res and sum(sequence[:]) == target:
                res.append(sequence[:])
            if pos == len(freq) or rest < freq[pos][0]:
                return
            backtrack(pos + 1, rest)
            most = min(rest // freq[pos][0], freq[pos][1])
            for i in range(1, most+1):
                sequence.append(freq[pos][0])
                backtrack(pos + 1, rest - i * freq[pos][0])
            sequence = sequence[:-most]

        res = []
        sequence = list()
        freq = sorted(collections.Counter(candidates).items())
        backtrack(0, target)
        return res


if __name__ == "__main__":
    s = Solution2()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(s.combinationSum2(candidates, target))
