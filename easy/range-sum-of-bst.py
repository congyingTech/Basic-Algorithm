# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        中序排序的考察
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root is None:
            return
        res = 0
        root_stack = []
        root_stack.append(root)
        while root_stack:
            while root:
                if root.left:
                    root_stack.append(root.left)
                root = root.left
            cur_root = root_stack.pop()
            cur_val = cur_root.val
            print(cur_val)
            if L<=cur_val<=R:
                res+=cur_val
            if cur_root.right:
                root_stack.append(cur_root.right)
                root = cur_root.right
        return res

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    s = Solution()
    res = s.rangeSumBST(root, 7, 15)
    print(res)