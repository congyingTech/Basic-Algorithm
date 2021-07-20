#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-07-20 01:39


给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：

例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
计算从根节点到叶节点生成的 所有数字之和 。

叶节点 是指没有子节点的节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

根左右框架
当前节点代表的值=10*上一层节点+当前节点的值
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, prevTotal):
            if not root:
                return 0
            # 根
            total = 10*prevTotal+root.val
            if not root.left and not root.right:
                return total

            return dfs(root.left, total) + dfs(root.right, total)

        return dfs(root, 0)


    def preOrderTraversal(self, root):
        sta = [root]
        res = []
        while sta:
            cur = sta.pop()
            res.append(cur.val)
            if cur.right:
                sta.append(cur.right)
            if cur.left:
                sta.append(cur.left)
        return res


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.left.right.left = TreeNode(6)
    root.left.right.left.right = TreeNode(2)

    print(Solution().preOrderTraversal(root))