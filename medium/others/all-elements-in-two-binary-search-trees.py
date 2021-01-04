# encoding:utf-8
# 问题描述：给定两个二叉树，要求输出两个二叉树的所有节点值的升序排序
# 解决方案：问题转换成两个有序数组的合并，先把二叉搜索树按照中序遍历给顺序遍历出来
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        res1 = []
        res2 = []
        self.inorder(root1, res1)
        self.inorder(root2, res2)
       
        res = self.localsort(res1, res2)
        return res
    def localsort(self, base_res, add_res):
        n = len(base_res)
        m = len(add_res)
        i,j = 0,0
        temp = []
        while i<n and j<m:
            if base_res[i]<=add_res[j]:
                temp.append(base_res[i])
                i+=1
            else:
                temp.append(add_res[j])
                j+=1
        if i==n:
            temp.extend(add_res[j:])
        if j==m:
            temp.extend(base_res[i:])
                       
        return temp

    def inorder(self, root, res):
        if root:
            if root.left:
                self.inorder(root.left, res)
            res.append(root.val)
            if root.right:
                self.inorder(root.right, res)        

if __name__ == "__main__":
    s = Solution()
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.left=TreeNode(0)
    root1.right.left=TreeNode(3)
    root2 = TreeNode(1)
    root2.left = TreeNode(0)
    root2.right = TreeNode(3)

    s.getAllElements(root1, root2)