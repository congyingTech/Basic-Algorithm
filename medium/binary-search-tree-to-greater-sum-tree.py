# encoding:utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    cursum = 0
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 右根左的遍历
        
        stack = [root]
        cursum = [0]
        count = 0
        while stack:
            while root.right:
                stack.append(root.right)
                root = root.right
            current_root = stack.pop()
            print(current_root.val)
            cursum.append(current_root.val+cursum[count])
            count += 1
            if current_root.left:
                stack.append(current_root.left)
                root = current_root.left 
        print(cursum)

    def bianli(self, root):
        if not root:
            return 
        self.bianli(root.right)
        self.cursum += root.val
        root.val = self.cursum
        self.bianli(root.left)


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(3)
    root.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)

    s.bstToGst(root)
    s.bianli(root)
