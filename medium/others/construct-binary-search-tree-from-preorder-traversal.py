# encoding:utf-8
# Definition for a binary binary_tree node.
"""
二叉查找树的中序遍历是有序的，所以可以根据中序遍历和已知的前序遍历确认一颗二叉查找树
output是层序遍历
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        # 左根右
        inorder = sorted(preorder)
        root = None
        root = self.recurse(preorder, inorder, root)
        return root

    def recurse(self, preorder, inorder, root):
        if len(preorder) < 1 and root:
            print('current node is leaf node!')
            return None
        node_value = preorder[0]
        inorder_index = inorder.index(node_value)
        left_tree_inorder_values = inorder[:inorder_index]
        right_tree_inorder_values = inorder[inorder_index+1:]
        left_tree_preorder_values = preorder[1:len(inorder[:inorder_index])+1]
        right_tree_preorder_values = preorder[len(inorder[:inorder_index])+1:]
        root = TreeNode(node_value)
        root.left = self.recurse(left_tree_preorder_values, left_tree_inorder_values,root)
        root.right = self.recurse(right_tree_preorder_values, right_tree_inorder_values, root)
        return root

if __name__ == '__main__':
    s = Solution()
    # 根左右
    preorder = [8,5,1,7,10,12]
             # [1,5,7,8,10,12]
    root = s.bstFromPreorder(preorder)
    print(root)
    