# encoding:utf-8
"""
问题描述：
判断一棵树是不是镜像二叉树
解决方案：
1)递归的方法：如果二叉树是镜像二叉树，那么它的左子树是等于右子树的
2)非递归的方法：可以用BFS层序遍历二叉树，然后设置两个队列，分别存左边的子树和右边的子树
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root,root)

    def isMirror(self, t1, t2):
        if not t2 and not t1:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val) & self.isMirror(t1.left, t2.right) & self.isMirror(t1.right, t2.left)

class Solution1(object):
    def isSymmetric(self, root):
        q = [root,root]
        while q:
            t1 = q.pop()
            t2 = q.pop()
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(8)
    root.left = TreeNode(6)
    root.right = TreeNode(6)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(5)
    print(s.isSymmetric(root))

    s1 = Solution1()
    print(s1.isSymmetric(root))