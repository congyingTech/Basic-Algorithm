# encoding:utf-8
# Definition for a binary tree node.
    #     4
    #    / \
    #   2   7
    #  / \
    # 1   3


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        pre = None
        head = root
        
        while head:
            pre = head
            if head.right and head.val<val:
                head = head.right
            elif head.left and head.val>val:
                head = head.left
            else:
                break
            
        
        if val>head.val:
            pre.right = TreeNode(val)
        else:
            pre.left = TreeNode(val)
        return root
            

if __name__ == "__main__":
    # root = TreeNode(4)
    # root.left = TreeNode(2)
    # root.right = TreeNode(7)
    # root.left.left = TreeNode(1)
    # root.left.right = TreeNode(3)
    # val = 0
    #[5,null,14,10,77,null,null,null,95,null,null]
    #4
    root = TreeNode(5)
    root.right = TreeNode(14)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(77)
    root.right.right.right = TreeNode(95)
    val = 4
    s = Solution()
    s.insertIntoBST(root, val)
