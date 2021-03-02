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
        超时的代码
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(index, temp):
            # 回溯结束的条件
            if len(temp) == k and sorted(temp[:]) not in res:
                res.append(sorted(temp[:]))
                return
            for i in range(index, n+1):
                if i not in temp:
                    temp.append(i)
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
    s = Solution2()
    n = 4
    k = 2
    s.combine(n, k)
