# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 12:51 上午
# @Author  : Mohn
# @FileName: 103-binary-tree-zigzag-level-order-traversal.py

# Definition for a binary tree node.
"""
锯齿形遍历 = bfs + 奇偶逆序
"""



class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        que = [root]
        while que:
            cur = que.pop(0)
            print(cur.val)
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)

    def levelPrintOrder(self, root):
        queue = [root]
        next_queue = []
        res = []
        level_data = []
        while queue:
           cur = queue.pop(0)
           level_data.append(cur.val)
           if cur.left:
               next_queue.append(cur.left)
           if cur.right:
               next_queue.append(cur.right)
           if not queue:
               res.append(level_data)
               queue = next_queue[:]
               next_queue = []
               level_data = []
        print(res)

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        next_queue = []
        level_data = []
        level_num = 0
        res = []

        while queue:
            cur = queue.pop(0)
            level_data.append(cur.val)
            if cur.left:
                next_queue.append(cur.left)
            if cur.right:
                next_queue.append(cur.right)
            if not queue:
                if level_num % 2 == 0:
                    res.append(level_data)
                else:
                    res.append(list(reversed(level_data)))
                queue = next_queue[:]
                next_queue = []
                level_data = []
                level_num += 1
        print(res)


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    Solution().levelOrder(root)
    Solution().levelPrintOrder(root)

    Solution().zigzagLevelOrder(root)

