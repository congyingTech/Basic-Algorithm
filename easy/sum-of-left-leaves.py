#encoding:utf-8

# Definition for a binary tree node.
#     3
#    / \
#   9  20
#     /  \
#    15   7
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        head = root
        left_node = []
        right_node = []
        tmp_root = [head]
        while tmp_root:
            head = tmp_root.pop()
            if head.left:
                left_node.append(head.left)
                tmp_root.insert(0, head.left)

            if head.right:
                right_node.append(head.right)
                tmp_root.insert(0, head.right)
        ans = 0
        for node in left_node:
            if not node.left and not node.right:
               ans+=node.val
        print(ans) 


    def sumOfLeftLeaves1(self, root):
        """
        递归版：先判断是不是左树，然后判断是否有左右子节点
        """
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves1(root.right)
        return self.sumOfLeftLeaves1(root.left)+self.sumOfLeftLeaves1(root.right)


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    s = Solution()
    s.sumOfLeftLeaves(root)
    a = s.sumOfLeftLeaves1(root)
    print(a)