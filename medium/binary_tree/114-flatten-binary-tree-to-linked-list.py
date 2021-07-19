# -*- coding: utf-8 -*-
# @Time    : 2021/7/19 3:09 下午
# @Author  : Mohn
# @FileName: 114-flatten-binary-tree-to-linked-list.py
"""
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


左右根的框架

"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        # 1.左子树flatten
        self.flatten(root.left)
        # 2.右子树flatten
        self.flatten(root.right)
        # 3.将左子树作为右子树
        left = root.left
        right = root.right
        root.left = None
        root.right = left
        # 4.将右子树作为左子树的末端
        p = root
        while p.right:
            p = p.right
        p.right = right

        return root
