# encoding:utf-8
"""
问题描述：给定一组数和滑动窗口的大小，找出所有滑动窗口里面最大的值
解决方案：
遍历数组的时候，设置一个双端queue：
1）左端口：当index与当前遍历的index的差值大于k时，把queue里面最左侧的最大数pop出来；
2）右端口：如果进来一个数nums[index]比queue所有值都大，那么把比queue中大的数都pop出去，然后追加index
3）如果遍历到的index大小大于等于窗口的大小，那么就取当前queue最左端的最大值。

直白来说，queue只保存两个值，一个是最大值，另一个是次大值，用于下一个窗口滑动。
queue的最左侧是最大值的index，后面是次大值的index，
"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:return []
        queue = []
        res = []
        n = len(nums)
        for i in range(n):
            # 当queue里面的兜不住滑动窗口的时候，就把queue最大的pop出来
            if i>=k and i-queue[0]>=k: 
                queue.pop(0)
            while queue and nums[queue[-1]]<=nums[i]:
                queue.pop()
            queue.append(i)
            if i>=k-1:
                res.append(nums[queue[0]])
        return res

if __name__ == "__main__":
    s = Solution()
    nums = [2,3,4,2,6,2,5,1]
    k = 3
    s.maxSlidingWindow(nums, k)