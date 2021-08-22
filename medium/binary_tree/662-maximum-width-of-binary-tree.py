#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-07-26 00:18
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        超时的解法
        fix：记录下每层的节点的位置
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        level_data = []
        next_level = []
        res = float('-inf')

        def findLevelMaxWidth(level_data):
            if set(level_data) == {None}:
                return -1

            left_index = 0
            right_index = len(level_data) - 1
            while left_index <= right_index:
                if level_data[left_index] == None:
                    left_index += 1
                if level_data[right_index] == None:
                    right_index -= 1
                if level_data[left_index] and level_data[right_index]:
                    break
            return right_index - left_index + 1

        while queue:
            cur_root = queue.pop(0)
            if cur_root:
                level_data.append(cur_root.val)
                if cur_root.left:
                    next_level.append(cur_root.left)
                else:
                    cur_root.left = TreeNode(None)
                    next_level.append(cur_root.left)
                if cur_root.right:
                    next_level.append(cur_root.right)
                else:
                    cur_root.right = TreeNode(None)
                    next_level.append(cur_root.right)
            else:
                level_data.append(None)

            if not queue:

                level_width = findLevelMaxWidth(level_data)
                if level_width==-1:
                    break
                res = max(res, level_width)

                queue = next_level[:]
                next_level = []
                level_data = []
        return res

    def widthOfBinaryTree1(self, root):
        """
        整体框架不变，level_data变成level_pos
        :param root:
        :return:
        """
        if not root:
            return
        queue = [(root, 0)]
        next_level = []
        level_pos = []
        res = 0
        while queue:
            item = queue.pop(0)
            cur = item[0]
            pos = item[2]
            level_pos.append(pos)
            if cur.left:
                next_level.append((cur.left, 2*pos))
            if cur.right:
                next_level.append((cur.right, 2*pos+1))
            if not queue:
                res = max(res, level_pos[-1] - level_pos[0] + 1)
                queue = next_level[:]
                next_level = []
                level_pos = []
        return res



if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(3)
    # root.right = TreeNode(2)
    # root.left.left = TreeNode(5)
    # root.left.left.left = TreeNode(6)
    # root.right.right = TreeNode(9)
    # root.right.right.right = TreeNode(7)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    print(Solution().widthOfBinaryTree(root))
