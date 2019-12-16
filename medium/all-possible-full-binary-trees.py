# encoding:utf-8
"""
问题描述：
给出结点的个数，求可能的满二叉树的层序遍历
解决方案：
注意：国内的满二叉树和国外的满二叉树不同，国内的满二叉树的每一层都很满，国外的满二叉树只要满足，所有结点要么是叶子结点或者，要么是有两个子结点即可
递归的思路，左右子树都是满二叉树，其中x个点构成左子树，y=N-1-x个点构成右子树
其中memory_dict = {0:[], 1:[TreeNode(0)]}是记录有N个结点可以构成的子树的结构，以时间换空间的做法。
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def print_tree(self):
        # 二叉树的层序遍历
        pass

class Solution(object):
    memory_dict = {0:[], 1:[TreeNode(0)]}
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N not in self.memory_dict:
            ans = []
            # 之所以可以两步走，是因为full binary tree一定有两个子结点
            # 当然也可以for x in range(N):
            for x in range(1, N-1, 2):
                y = N-x-1
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        # left 和 right 是所有建成的子树的字典，下面的操作就是和跟结点组合
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            self.memory_dict[N] = ans
        return self.memory_dict[N]


if __name__ == "__main__":
    s  = Solution()
    N = 7
    s.allPossibleFBT(N)
        