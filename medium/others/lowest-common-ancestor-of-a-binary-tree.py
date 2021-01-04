# encoding:utf-8
"""
问题描述：
给定一棵树，和两个结点，寻找这两个结点的最近的父节点，LCA问题
解决方案：
1）递归的思想+flag标签
2）非递归遍历+dict的思路
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    # 递归的解法
    def __init__(self):
        self.ans = None
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurveFindCommon(root, p, q):
            if not root:
                return False
            left = recurveFindCommon(root.left, p, q)
            right = recurveFindCommon(root.right, p, q)
            mid = root is p or root is q # mid是p或者q中的一个的时候开始回溯转变False为True
            if left + right + mid >=2:  # 一旦大于两个True，就可以确定该结点是最近的共同的父节点
                self.ans = root

            return mid or left or right # mid或者left或right中有一个是True的，那么回溯到上一层就可以改变为True
            
        recurveFindCommon(root, p, q)   
        return self.ans
        
class Solution2(object):
    # 非递归+dict
    def lowestCommonAncestor(self, root, p, q):
        dic = {root:None}
        
        records = [root]
        while root:
            if root.left and root.left not in dic:
                records.append(root.left)
                dic[root.left] = root
                root = root.left
            elif root.right and root.right not in dic:
                records.append(root.right)
                dic[root.right] = root
                root = root.right
            elif records:
                root = records.pop()
            else:
                break
        # 接下来，找到p所有的父节点保存到set中，然后遍历q的父节点，看是否在p的set中出现
        ancestor = set()
        while p:
            ancestor.add(p)
            p = dic[p]
        while q not in ancestor:
            q = dic[q]
        return q
        

class Solution3(object):
    # 二叉树是BST树：当前遍历到的结点比p和q都大，那么pq的最近公共结点一定在左子树，如果比p大比q小，那么当前就是最近公共结点
    def lowestCommonAncestor(self, root, p, q):
        if root.val>q.val and root.val>p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

if __name__ == "__main__":
    s1 = Solution1()
    s2 = Solution2()
    # [3,5,1,6,2,0,8,null,null,7,4]
    p = TreeNode(2)
    q = TreeNode(8)
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = p
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    res1 = s1.lowestCommonAncestor(root, p, q)
    # res2 = s2.lowestCommonAncestor(root, p, q)
    # print(res1.val, res2.val)

    s3 = Solution3()
    p = TreeNode(5)
    q = TreeNode(3)
    root = TreeNode(9)
    root.left = TreeNode(7)
    root.right = TreeNode(10)
    root.left.left = p
    root.left.right = TreeNode(8)
    root.left.left.left = q
    root.right.right = TreeNode(11)
    res = s3.lowestCommonAncestor(root, p, q)
    print(res.val)
