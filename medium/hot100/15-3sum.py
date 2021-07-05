"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

解题思路：排序+指针
a+b+c=0
保持不重复的方法就是排序，保证了a>b>c
a,b,c需要三层循环，当a确定的情况下，只有b和c时，b+c = -a是确定的，意味着b往后遍历时b越来越大，那么c越来越小，bc可以放到同一层循环中
这样c可以从第二层循环数组的最后一位开始随着b的循环左移。
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        n = len(nums)
        res = []

        for i, a in enumerate(nums):
            # nums有重复的元素，去掉，且要大于0的情况
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target_bc = -a
            k = n - 1
            for j in range(i+1, n):
                # nums有重复的元素，判断去掉
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                # 保证b在c的左边，根据b的位置，找到b+c>target_bc且b+c最小的c的位置，此时再往前，要么等于，要么小于
                while k > j and nums[j] + nums[k] > target_bc:
                    k -= 1
                if k == j:
                    break
                if nums[j] + nums[k] == target_bc:
                    res.append([nums[i], nums[j], nums[k]])
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, -1, -1, 0]
    print(s.threeSum(nums))
