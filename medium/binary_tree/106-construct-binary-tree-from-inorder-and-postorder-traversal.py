#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-07-20 01:28
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return
        root_val = postorder[-1]
        root = TreeNode(root_val)
        inorder_index = inorder.index(root_val)
        left_inorder = inorder[:inorder_index]
        right_inorder = inorder[inorder_index+1:]
        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):len(postorder)-1]

        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)

        return root


if __name__ == "__main__":
    root = Solution().buildTree([9,3,15,20,7], [9,15,7,20,3])
    queue = [root]
    level_data = []
    res = []
    next_level = []
    while queue:
        cur = queue.pop(0)
        level_data.append(cur.val)
        if cur.left:
            next_level.append(cur.left)
        if cur.right:
            next_level.append(cur.right)
        if not queue:
            res.append(level_data)
            queue = next_level[:]
            next_level = []
            level_data = []

    print(res)



