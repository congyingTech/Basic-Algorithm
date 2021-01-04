# encoding:utf-8
# 问题描述：一颗二叉树上的每个节点都有一个硬币的值，有些是0，是0的节点需要非0的节点分享多余的硬币
# 解决方案：

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distributeCoins(self, root):
        self.ans = 0

        def dfs(node):
            if not node: return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.ans

# class Solution(object):
#     def distributeCoins(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root.val!=1:
#             level_info = {root:0}
#         else:
#             level_info = {}
#         if root.left:
#             level = 1
#             self.dfs_left(root.left, level, level_info)
#         if root.right:
#             level = -1
#             self.dfs_right(root.right, level, level_info)
#         res = 0
#         level_needs = []
#         for node in level_info:
#             if node.val>0:
#                 level_needed = level_info[node]
#             else:
#                 level_needs.append(level_info[node])
#         for level in level_needs:
#             res += abs(level_needed-level)
#         return res
               
            
#     def dfs_left(self, root, level, level_info):
#         if root:
#             if root.left:
#                 self.dfs_left(root.left, level+1, level_info)
#             if root.right:
#                 self.dfs_left(root.right, level+1, level_info)
        
#         if root not in level_info and root.val!=1:
#             level_info[root] = level
#     def dfs_right(self, root, level, level_info):

#         if root:
#             if root.left:
#                 self.dfs_right(root.left, level-1, level_info)
#             if root.right:
#                 self.dfs_right(root.right, level-1, level_info)
        
#         if root not in level_info and root.val!=1:
#             level_info[root] = level
       
       
if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(0)
    #root.left.right = TreeNode(3)
    root.right = TreeNode(0)
    
    print(s.distributeCoins(root))