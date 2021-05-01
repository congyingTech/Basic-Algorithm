"""
寻找完全二叉树的最后一个节点
"""


class TreeNode(object):
    def __init__(self, val):
          self.left = None
          self.right = None
          self.val = val


class Solution(object):
    def depth(self, root):
        cnt = 0
        while root:
             root = root.left
             cnt += 1
        return cnt
 
    def lastnode(self, root):
        if not root:
           return None
        if not root.left and not root.right:
            return root
        left_level = self.depth(root.left)
        right_level = self.depth(root.right)
        if left_level == right_level:
            return self.lastnode(root.right)
        else:
            return self.lastnode(root.left)


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    last_node = s.lastnode(root)
    print(last_node.val)








