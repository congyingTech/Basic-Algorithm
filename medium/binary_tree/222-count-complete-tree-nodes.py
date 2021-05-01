# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 11:18 上午
# @Author  : Mohn
# @FileName: 222-count-complete-tree-nodes.py
"""
完全二叉树的叶子结点

"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    ans = 0

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_count = self.countNodes(root.left)
        right_count = self.countNodes(root.right)
        return left_count+right_count+1


class Solution1(object):
    """
    利用二分法的思想，左右子树一样高的时候，左子树一定是满二叉树，总共的节点的个数=满左子树(2^left_level-1+1) + 右子树(self.countNodes(self.right))
    左右子树不一样高的时候，右子树一定是满的，节点个数=满右子树+左子树
    """
    def depth(self, root):
        cnt = 0
        while root:
              root = root.left
              cnt += 1
        return cnt

    def countNodes(self, root):
        if not root:
           return 0
        left_level = self.depth(root.left)
        right_level = self.depth(root.right)
        if left_level == right_level:
            return 2**left_level + self.countNodes(root.right)
        else:
            return 2**right_level + self.countNodes(root.left)


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left = TreeNode(4)
    print(s.countNodes(root))
    s1 = Solution1()
    print(s1.countNodes(root))


