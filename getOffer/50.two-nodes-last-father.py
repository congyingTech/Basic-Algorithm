# encoding:utf-8
"""
问题描述：
给定两个树结点寻找它俩的最近的公共父节点
解决方案：
mine思路1）如果是二叉树的话，可以遍历树，并保存一个dict{结点：父节点}，然后一次查询dict，直到查询到的父节点相同，返回该父节点。
该思路和lowest-common-ancestor-of-a-binary-tree的approach2相同，时间空间复杂都是O(N)
思路2）如果不是二叉树，且这个树有结点指向父节点的指针的话，可以转化成寻找两个链表的最早公共结点
思路3）如果是二叉搜索树，那么可以根据二叉搜索树的性质：如果根的权值处于 node1 和 node2 之间,则根就是它们的最低公共祖先结点如果根的权值比 node1 和 node2 都大,则它们的最低公共祖先结点在根的左子树中如果根的权值比 node1 和 node2 都小,则它们的最低公共祖先结点在根的右子树中
思路4）如果是普通二叉树，且没有结点指向父节点，那么可以用两个链表保存从根到该结点的链表的路径，转换成求两个链表的最后公共结点。
"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution1(object):
    # 树是普通的二叉树，用递归的思路解决
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
            mid = root is p or root is q  # mid是p或者q中的一个
            if left + right + mid >= 2:
                self.ans = root

            return mid or left or right  # mid或者left或right中有一个是True的，那么回溯到上一层就可以改变为True

        recurveFindCommon(root, p, q)
        return self.ans


class Solution2(object):
    # 树是普通二叉树，用非递归dfs+dict
    def lowestCommonAncestor(self, root, p, q):
        dic = {root: None}

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
        if root.val > q.val and root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root


if __name__ == "__main__":
    s1 = Solution1()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    p = TreeNode(0)
    q = TreeNode(10)
    root.left.left.right = p
    root.right.right.left = q
    s1.lowestCommonAncestor(root, p, q)
