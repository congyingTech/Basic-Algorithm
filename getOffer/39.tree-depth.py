# encoding:utf-8
"""
问题描述：
题目1:求二叉树的深度，从根到叶子结点依次经过的结点形成的树的一条路径，最长路径的长度是二叉树的深度。
题目2:输入一颗二叉树的根节点，判断该树是不是平衡二叉树。平衡二叉树的定义是某二叉树中任意子树的深度相差不超过1，就是平衡二叉树。
解决方案：
深度优先遍历。
"""
class TreeNode(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class Solution(object):
    def findTreeDepth(self,root):
        if not root:
            return 0
        left_depth = self.findTreeDepth(root.left)
        right_depth = self.findTreeDepth(root.right)
        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1

class Solution1(object):
    def findTreeDepth(self,root):
        if not root:
            return 0
        left_depth = self.findTreeDepth(root.left)
        right_depth = self.findTreeDepth(root.right)
        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1

    def isBalanceTree(self, root):
        if not root:
            return True
        left_depth = self.findTreeDepth(root.left)
        right_depth = self.findTreeDepth(root.right)
        diff = abs(left_depth-right_depth)
        if diff > 1:
            return False
        return self.isBalanceTree(root.left) and self.isBalanceTree(root.right)

if __name__ == "__main__":
    s = Solution()
    s1 = Solution1()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(s.findTreeDepth(root))
    print(s1.isBalanceTree(root))