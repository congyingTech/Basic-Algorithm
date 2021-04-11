# Definition for a binary binary_tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
#中序遍历二叉树，然后求相邻数字的差求最小
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        rootlist=[]
        def bianli(root):
            if root == None:
                return 
            if root.left:
                bianli(root.left)
            rootlist.append(root.val)
            if root.right:
                bianli(root.right)
            return rootlist
        bianli(root)
        sublist = []
        for i,e in enumerate(rootlist):
            if i+1<len(rootlist):
                sublist.append(rootlist[i+1]-e)
        return min(sublist)

if __name__ == '__main__':
    root = TreeNode(2)         
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.right.right = TreeNode(5)
    s = Solution()
    print(s.getMinimumDifference(root))
            
            