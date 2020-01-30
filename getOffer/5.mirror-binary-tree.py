# encoding:utf-8
"""
问题描述：
   8
 6   10
5 7 9 11
的镜像是：
    8
 10   6
11 9 7 5
解决方案：
递归的想法，就是从根节点开始遍历子节点，直到遇到叶子结点，当有左右子节点的时候交换左右子节点
1)就地递归
2)创建新树递归

"""

class TreeNode(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class Solution(object):
    """
    创建新的树
    """
    def findMirrorTree(self, root):
        if not root:
            return
        newTree = TreeNode(root.val)
        if root.left and root.right:
            newTree.left = self.findMirrorTree(root.right)
            newTree.right = self.findMirrorTree(root.left)
        elif root.left and not root.right:
            newTree.right = self.findMirrorTree(root.left)
        else:
            newTree.left = self.findMirrorTree(root.right)
        return newTree

class Solution1(object):
    def findMirrorTree(self, root):
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.findMirrorTree(root.left)
        self.findMirrorTree(root.right)
        return root

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(8)
    root.left = TreeNode(6)
    root.right = TreeNode(10)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(11)
    newTree = s.findMirrorTree(root)
    print(1)
    root1 = s.findMirrorTree(root)
    print(2)