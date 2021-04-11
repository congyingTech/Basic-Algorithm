# Definition for a binary binary_tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def searchBST(self, root, val):
        
        # if val == root_val:
        #     res_root = root
        if root and val<root.val :
            return self.searchBST(root.left, val)
        if root and val>root.val :
            return self.searchBST(root.right, val)
        return root       




# class Solution(object):
#     def searchBST(self, root, val):
#         """
#         :type root: TreeNode
#         :type val: int
#         :rtype: TreeNode
#         """
#         root_val = root.val
#         if val == root_val:
#             res_root = root
#         if val<root_val and root.left:
#             self.searchBST(root.left, val)
#         if val>root_val and root.right:
#             self.searchBST(root.right,val)
#         return res_root    

if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root_val = root.val
    s = Solution()
    res = s.searchBST(root, 3)
    print(res.val)
