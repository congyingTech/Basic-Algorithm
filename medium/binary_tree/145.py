# -*- coding: utf-8 -*-
# @Time    : 2021/5/6 2:44 下午
# @Author  : Mohn
# @FileName: 145.py
"""
二叉树后序遍历
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    ans = []

    def postorderTraversal1(self, root):
        # 递归解法
        if not root:
            return
        if root.left:
            self.postorderTraversal1(root.left)
        if root.right:
            self.postorderTraversal1(root.right)
        return self.ans.append(root.val)

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        while res:
            print(res.pop().val)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.right = TreeNode(5)
    s = Solution()
    print(s.postorderTraversal(root))
