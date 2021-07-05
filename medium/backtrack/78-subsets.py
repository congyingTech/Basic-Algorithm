"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

 

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets

解题思路：
【子集问题特点】
1.元素不要求有序，所以是index+1
2.子集合的每一个元素不可以重复，所以是执行+1操作
3.输入的元素互不相同，不需要去重操作

"""


class Solution1(object):
    """
    超时的代码
    """
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)

        def backtrack(pos, temp):
            # inner_temp = sorted(temp).copy()
            # [:]和copy同样是浅拷贝，浅拷贝是引用，原有的对象进行增删改的时候，拷贝后的对象也会随之变化；深拷贝是拷贝子对象和父对象，原有的对象变化，不会产生变化。
            # if sorted(temp[:]) not in res:
            #     res.append(sorted(temp[:]))
            if temp[:] not in res:
                res.append(temp[:])
            # if index == n:
            #     return
            for index in range(pos, n):
                if nums[index] not in temp:
                    temp.append(nums[index])
                    backtrack(index+1, temp[:])
                    temp.pop()
        backtrack(0, [])
        return res


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)

        def backtrack(pos, temp):
            # if temp not in res:
            #     res.append(temp)
            # # if index == n:
            # #     return
            # for i in range(index, n):
            #     if nums[i] not in temp:
            #         temp.append(nums[i])
            #         backtrack(index+1, temp)
            if temp not in res:
                res.append(temp)
            for index in range(pos, n):
                backtrack(index + 1, temp+[nums[index]])

        backtrack(0, [])
        return res


if __name__ == "__main__":
    nums = [4, 3, 2, 1]
    s = Solution1()
    # 相较于78题，之所以不用排序，是因为输入元素无重复。
    res = s.subsets(nums)
    print(res)
