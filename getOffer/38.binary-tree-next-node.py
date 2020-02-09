# encoding:utf-8
"""
问题描述：
给定一棵二叉树和其中一个结点，如何找到中序遍历顺序的下一个结点
解决方案：
如果一个结点有右子树，那么它的下一个结点是右子树的最右结点，
如果一个结点没有右子树且它当前处父节点的左子树，那么它的下一个结点是父节点，
如果一个结点没有右子树且它当前处父节点的右子树，那么往上遍历，直到找到该结点处于某父节点的左子树的父结点，就是下一个输出。
"""
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None
    

class Solution(object):
    def binaryTreeNextNode(self, root):
        if not root:
            return None
        if root.right:
            root = root.right
            while root.left:
                root = root.left
            return root
        else:
            while root.next:
                if root == root.next.left:
                    return root.next
                else:
                  root = root.next

        return None  


if __name__ == "__main__":
    s = Solution()
    a =  TreeNode('a')
    b = TreeNode('b')
    c = TreeNode('c')
    d = TreeNode('d')
    e = TreeNode('e')
    f = TreeNode('f')
    g = TreeNode('g')
    h = TreeNode('h')
    i = TreeNode('i')
    
    a.left = b
    a.right = c
    b.next = a
    c.next = a
    b.left = d
    b.right = e
    d.next = b
    e.next = b
    e.left = h
    e.right = i
    h.next = e
    i.next = e
    c.left = f
    c.right = g
    f.next = c
    g.next = c
    # 该树的中序遍历是d b h e i a f c g
    # e的下一个结点应该是i
    print(s.binaryTreeNextNode(g).val)