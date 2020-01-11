# encoding:utf-8
# 问题描述：给定一个二叉树，求树最深的叶子结点的和值。
# exp：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# return 15
# 解决方案：DFS+dict，不要太在意递归的细节，只要按层数level递增就行

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = 0
        res = {}
        node_list = [root.val]
        self.dfs(root, level, res, node_list)
        print(node_list)
        return res[max(res)]
    
    
    def dfs(self, node, level, res, node_list):        
        if node:
            if node.left:
                node_list.append(node.left.val)
                self.dfs(node.left, level+1, res, node_list)
            if node.right:
                node_list.append(node.right.val)
                self.dfs(node.right, level+1, res, node_list)
                    
        if level not in res:
            res[level] = node.val
        else:
            res[level] += node.val
            

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(6)
    root.left = TreeNode(7)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(3)
    root.left.left.left = TreeNode(9)
    root.left.right.left = TreeNode(1)
    root.left.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)

    s.deepestLeavesSum(root)
