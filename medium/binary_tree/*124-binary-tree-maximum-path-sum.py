#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-07-19 23:50

路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

和543题比较相似

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.max_sum = float("-inf")

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxGain(root):
            if not root:
                return 0

            # 左子树的价值
            left_max = max(maxGain(root.left), 0)
            # 右子树的价值
            right_max = max(maxGain(root.right), 0)
            # 回溯到节点的价值和
            temp = left_max + right_max + root.val
            self.max_sum = max(temp, self.max_sum)
            # 非叶子节点的贡献值等于
            return root.val + max(left_max, right_max)
        maxGain(root)
        return self.max_sum


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    root.left.right = TreeNode(15)
    print(s.maxPathSum(root))



