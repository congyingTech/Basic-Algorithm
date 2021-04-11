# Definition for a binary binary_tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#超时了，原因应该是后面的循环的原因

#这个是根左右的前序遍历结果
class Solution(object):
    
    def tree2str(self, t):
        res = []
        def getTreeList(t):
            if t == None:
                return res
            res.append('%d'%t.val)
            if t.left != None:
                res.append('(')
                res.append(getTreeList(t.left))
                res.append(')')
            if t.right != None:
                if t.left == None and t.right != None:
                    res.append('()')
                res.append('(')
                res.append(getTreeList(t.right))
                res.append(')')
        getTreeList(t)
        for e in res:
            if e == None:
                res.remove(e)
        return ''.join(res)
if __name__ == '__main__':
    s = Solution()
#         1
#      /   \
#     2     3
#    /    
#   4 
    t = TreeNode(0)
    #t.left = TreeNode(2)
    t.right = TreeNode(0)
    #t.left.right = TreeNode(4)
    t.right.right = TreeNode(0)
    t.right.right.right = TreeNode(0)
    print(s.tree2str(t))
