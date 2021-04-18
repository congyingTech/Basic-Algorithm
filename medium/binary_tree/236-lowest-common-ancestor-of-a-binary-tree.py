#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-04-18 00:42

二叉树的最近公共祖先：
https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/

后序遍历，可以左右根，保证了遍历到p和q的同时，遍历了最近公共祖先。

"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        lson = self.lowestCommonAncestor(root.left, p, q)
        rson = self.lowestCommonAncestor(root.right, p, q)
        if not lson and not rson:
        # 情况1：左右子树都没有，说明是空的
            return
        if not lson:
        # 情况2：没有左子树，说明最近公共祖先在右子树
            return rson
        if not rson:
        # 情况3：没有右子树，说明最近公共祖先在左子树
            return lson
        # 情况4：左右子树都有，说明公共子树是root
        return root


if __name__ == "__main__":
    s = Solution()
    # root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    p = TreeNode(5)
    q = TreeNode(4)

    s.lowestCommonAncestor(root, p, q)