# encoding:utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 递归终止条件：
        if len(nums)==0:
            return

        max_num = max(nums)
        max_index = nums.index(max_num)
        root = TreeNode(max_num)

        if max_index!=0:
            # 如果左边还有数，那么就进入左递归
            root.left = self.constructMaximumBinaryTree(nums[:max_index])
        if max_index!=len(nums)-1:
            # 如果右边还有数，就进入右递归
            root.right = self.constructMaximumBinaryTree(nums[max_index+1:])
        return root    


if __name__ == "__main__":
    s = Solution()
    nums = [3,2,1,6,0,5]
    root = s.constructMaximumBinaryTree(nums)
