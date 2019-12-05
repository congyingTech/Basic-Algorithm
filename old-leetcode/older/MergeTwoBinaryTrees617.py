#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: 
        """
        #两棵树为空的情况下返回另一棵树
        if t1 == None :
            return t2
        if t2 == None:
            return t1
        #根左右的进行合并
        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1   
        
    def bianli(self,t):
        print(t.val)
        if t.left:
            self.bianli(t.left)
        if t.right:
            self.bianli(t.right)   
            

if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)
    t1.left.left = TreeNode(5)
    
    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    t2.left.right = TreeNode(4)
    t2.right.right = TreeNode(7)
    
    s = Solution()
    t = s.mergeTrees(t1, t2)
    
    s.bianli(t)
        