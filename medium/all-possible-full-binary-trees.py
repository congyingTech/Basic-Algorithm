# encoding:utf-8
"""
问题描述：
给出结点的个数，求可能的满二叉树的层序遍历
解决方案：
国内的满二叉树和国外的满二叉树不同，国内的满二叉树的每一层都很满，国外的满二叉树只要满足，所有结点要么是叶子结点或者，要么是有两个子结点即可
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """