# encoding:utf-8
"""
问题描述：
s=   3
    / \
   4   5
  / \
 1   2
t= 4 
  / \
 1   2

给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。


解决方案：
辅助函数isMatch是判断两个树结构是否完全一致，可以判断s和t是否完全一致，
判断的条件是: s.val == t.val and self.isMatch(s.left, t.left) and self.isMatch(s.right, t.right)
或者判断s的子树（左右）是否和t一致
"""
# Definition for a binary binary_tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归的方法
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if self.isMatch(s,t):
            return True
        if not s:
            return False
        # 上面的isMatch是s和t的全匹配，如果无法全匹配的话，看s的左右子树可不可以全匹配
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isMatch(self, s,t):
        if not (s and t):
            return s is t
        return s.val == t.val and self.isMatch(s.left, t.left) and self.isMatch(s.right, t.right)
        

if __name__ == "__main__":
    solve = Solution()
    s = TreeNode(3)
    s.left = TreeNode(4)
    s.right = TreeNode(5)
    s.left.left = TreeNode(1)
    s.left.right = TreeNode(2)

    t = TreeNode(4)
    t.left = TreeNode(1)
    t.right = TreeNode(2)
    print(solve.isSubtree(s,t))