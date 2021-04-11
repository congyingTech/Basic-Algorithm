# Definition for a binary binary_tree node.
#应该考虑层序遍历，把每一层的节点值逆置
from platform import node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return 0
        que = [root]
        while que:
            q = que.pop(0)
            if q.left != None:
                que.append(q.left)
            if q.right != None:
                que.append(q.right)
            q.left, q.right = q.right,q.left
        return root
    
    #对tree进行前序遍历
    def pre(self, node):   
        if node == None:
            return 0
        print(node.val)
        if node.left:
            self.test(node.left)
        if node.right:
            self.test(node.right)
 
       
            
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.right = TreeNode(4)
    root.left.right.right = TreeNode(3)
    s = Solution()
    tree = s.invertTree(root)
    s.test(tree)
    
    
    
    
    