"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations

"""


class Solution1(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(pos, temp):
            # 回溯结束的条件
            if len(temp) == k:
                res.append(temp[:])
                return
            for index in range(pos, n+1):
                temp.append(index)
                backtrack(index+1, temp[:])
                temp.pop()

        res = []
        backtrack(1, [])
        print(res)
        return res


class Solution2(object):
    def combine(self, n, k):
        def backtrack(pos, temp):
            if len(temp) == k:
                res.append(temp)
                return
            for index in range(pos, n+1):
                backtrack(index+1, temp+[index])
        res = []
        backtrack(1, [])
        print(res)
        return res


if __name__ == "__main__":
    s = Solution1()
    n = 4
    k = 2
    # 相较于40题，之所以不用排序，是因为本来从1到n就是一个有序的无重复序列。
    s.combine(n, k)
