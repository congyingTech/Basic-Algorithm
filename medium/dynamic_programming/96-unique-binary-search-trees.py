"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees
dp思路：
二叉搜索树：根结点左子树的值小于根结点的值，根结点右子树的值大于根结点的值



需要有两个状态：
G(n)表示的是n长度的序列组成的不同的二叉搜索树的个数
G(n) = F(1,n) + F(2,n) + ... + F(i,n) + ... + F(n,n)
F(i,n)表示的是以i为根结点，n长度的序列组成的不同的二叉搜索树的个数
左右两边子树的笛卡尔积
F(i,n) = G(i-1) * G(n-i)
G(n)可以写成关于G(i-1)*G(n-i)的求和表达式

G(n) = ∑ F(i,n)
G(n) = ∑ G(i-1)*G(n-i)
其中 1 <=i <= n , G(0) = 1 , G(1) = 1
"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0] * (n+1)
        G[0] = 1
        G[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1]*G[i-j]
        return G[n]


if __name__ == "__main__":
    s = Solution()
    n = 3
    print(s.numTrees(n))
