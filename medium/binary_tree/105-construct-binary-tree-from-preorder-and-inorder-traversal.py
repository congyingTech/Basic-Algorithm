#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-04-18 00:20
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return
        root_val = preorder.pop(0)
        root_node = TreeNode(root_val)
        # 定位可以用hash表快速定位
        index = 0
        while inorder[index] != root_val:
            index += 1
        inorder_left_val = inorder[:index]
        inorder_right_val = inorder[index+1:]
        preorder_left_val = preorder[:len(inorder_left_val)]
        preorder_right_val = preorder[len(inorder_left_val):]
        root_node.left = self.buildTree(preorder_left_val, inorder_left_val)
        root_node.right = self.buildTree(preorder_right_val, inorder_right_val)
        return root_node


if __name__ == "__main__":
    s = Solution()
    # 根左右
    preorder = [3, 9, 20, 15, 7]
    # 左根右
    inorder = [9, 3, 15, 20, 7]
    s.buildTree(preorder, inorder)
