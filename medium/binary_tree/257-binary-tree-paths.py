#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-07-21 00:22

所有路径，根左右，前序遍历，因为要打印出来，记得pop()
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        path = []

        def dfs(root):
            if not root:
                return
            path.append(str(root.val))
            if not root.left and not root.right:
                paths.append("->".join(path))

            # 回溯就是多叉树的前序遍历(dfs)，这里只能向左和向右走，所以不用循环遍历可走的选项
            dfs(root.left)
            dfs(root.right)
            path.pop()
        dfs(root)
        return paths


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(Solution().binaryTreePaths(root))
