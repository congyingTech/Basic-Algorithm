#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-07-21 22:15

解题思路：
以某一个树节点出发，该节点偷与不偷
1）偷该节点
val1 = node.val + dfs(node.left.left) + dfs(node.left.right)
                + dfs(node.right.left) + dfs(node.right.right)
2）不偷该节点
val2 = dfs(node.left) + dfs(node.right)
3）记忆化，进行剪枝
self.max_rob = {}
self.max_rob[node] = max(val1, val2)

"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.max_rob = {}

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0
            if self.max_rob and self.max_rob.get(root, None):
                return self.max_rob[root]
            # 偷该节点
            val1 = 0
            if root.left:
                val1 += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                val1 += dfs(root.right.left) + dfs(root.right.right)

            val1 += root.val
            # 不偷该节点
            val2 = dfs(root.left) + dfs(root.right)
            self.max_rob[root] = max(val1, val2)
            return self.max_rob[root]
        res = dfs(root)
        return res


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)
    print(Solution().rob(root))
