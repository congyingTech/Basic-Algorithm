# encoding:utf-8
"""
问题描述：
二叉树的层序遍历
解决方案：
用一个队列记录当前遍历的节点，把当前节点从队列输出的同时把其左右子节点入队列
"""

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class Solution1(object):
    # 按层遍历且追层返回
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [root]
        res = []
        
        while queue:
            level_res = []
            next_level = []
            for node in queue:
                level_res.append(node.val)
                if node.left and node.right:
                    next_level.append(node.left)
                    next_level.append(node.right)
                elif node.left:
                    next_level.append(node.left)
                elif node.right:
                    next_level.append(node.right)
            queue = next_level
            res.append(level_res)

        return res[::-1]
        

class Solution(object):
    def printBinaryTreeBylevel(self, root):
        queue = [root]
        while queue:
            cur = queue[0]
            print(cur.val)
            queue.remove(cur)
            if cur.left and cur.right:
                queue.append(cur.left)
                queue.append(cur.right)
            elif cur.left:
                queue.append(cur.left)
            elif cur.right:
                queue.append(cur.right)

if __name__ == "__main__":
    solve = Solution1()
    s = TreeNode(3)
    s.left = TreeNode(4)
    s.right = TreeNode(5)
    s.left.left = TreeNode(1)
    s.left.right = TreeNode(2)
    s.left.right.left = TreeNode(10)
    s.left.right.right = TreeNode(11)

    s = TreeNode(1)
    s.left = TreeNode(2)
    s.left.left = TreeNode(4)
    s.right = TreeNode(3)
    s.right.right = TreeNode(5)

    print(solve.levelOrderBottom(s))