# encoding:utf-8
# 二叉树深度搜索


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def isSafe(self, node, temp):
        if node.val not in temp:
            return True
        else:
            return False

    def dfs(self, root, temp, res):
        
        if root.left == None and root.right==None:
            for i in temp:
                if i not in res:
                    res.append(i)

        current_possible_node = []
        if root.left:
            current_possible_node.append(root.left)
        if root.right:
            current_possible_node.append(root.right)

        for node in current_possible_node:
            if self.isSafe(node, temp):
                temp.append(node.val)
                self.dfs(node, temp, res)
                temp.pop()

    def dfsSolution(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        temp = [root.val]
        
        res = []
        self.dfs(root, temp, res)
        print(res)

class Solution1(object):
    def dfsSolution(self, root):
        """
        非递归的方法：用node_record存储遍历过的节点，方便进行回溯
        """
        res = [root.val]
        node_record = [root]
        while root:
            if root.left and root.left.val not in res:
                res.append(root.left.val)
                node_record.append(root.left)
                root = root.left
            elif root.right and root.right.val not in res:
                res.append(root.right.val)
                node_record.append(root.right)
                root = root.right
            elif node_record:
                root = node_record.pop()
            else:
                break
        print(res)

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.right.right = TreeNode(8)
    root.left.left.left = TreeNode(7)
    root.right.right.left = TreeNode(10)


    s.dfsSolution(root)

    s1 = Solution1()
    s.dfsSolution(root)