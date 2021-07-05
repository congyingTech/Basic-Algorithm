# -*- coding: utf-8 -*-
# @Time    : 2021/5/6 2:01 下午
# @Author  : Mohn
# @FileName: 199-binary-tree-right-side-view.py

# Definition for a binary tree node.
"""
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

非递归：
层序遍历，每一层的最后一个元素。
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = [root]
        level_data = []
        next_level_node = []
        res = []
        while queue:
            cur_node = queue.pop(0)
            level_data.append(cur_node.val)
            if cur_node.left:
                next_level_node.append(cur_node.left)
            if cur_node.right:
                next_level_node.append(cur_node.right)
            if not queue:
                queue = next_level_node
                res.append(level_data[-1])
                level_data = []
                next_level_node = []
        return res


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    print(s.rightSideView(root))
