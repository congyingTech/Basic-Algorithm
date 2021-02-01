"""
如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。

例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。

给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。

示例 1:

输入: [1,7,4,9,2,5]
输出: 6
解释: 整个序列均为摆动序列。
示例 2:

输入: [1,17,5,10,13,15,10,5,16,8]
[16, -12, 5, 3, 2, -5, -5, 11, -8]
输出: 7
解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wiggle-subsequence

dp的思想：
定义up和down两种状态：
up[i]表示第i个元素的前一个gap是上升的摆动序列
down[i]表示第i个元素的前一个gap是下降的摆动序列
当nums[i] >= nums[i-1]时，i之前的这个gap为上升
down[i]只能是down[i-1]，因为前一个gap是上升
up[i]可以是up[i-1]或者down[i-1]+1
所以状态转移公式：
up[i] = up[i-1] if nums[i]<=nums[i-1]
up[i] = max(up[i-1], down[i-1]+1) if nums[i]>nums[i-1]
down[i] = down[i-1] if nums[i]>=nums[i-1]
down[i] = max(down[i-1], up[i-1]+1) if nums[i]<nums[i-1]
max_len = max(up[i], down[i])
"""


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return 1
        up = [0]*n
        up[0] = 1
        down = [0]*n
        down[0] = 1
        max_len = 0
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                up[i] = up[i-1]
                down[i] = max(down[i-1], up[i-1]+1)
            elif nums[i] > nums[i-1]:
                up[i] = max(up[i-1], down[i-1]+1)
                down[i] = down[i-1]
            else:
                up[i] = up[i-1]
                down[i] = down[i-1]
            max_len = max(up[i], down[i])
        return max_len


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1]
    print(s.wiggleMaxLength(nums))




