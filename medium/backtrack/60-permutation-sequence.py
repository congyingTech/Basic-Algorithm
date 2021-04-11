"""
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

 

示例 1：

输入：n = 3, k = 3
输出："213"
示例 2：

输入：n = 4, k = 9
输出："2314"
示例 3：

输入：n = 3, k = 1
输出："123"
 

提示：

1 <= n <= 9
1 <= k <= n!


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-sequence

解题思路：
在全排列的基础上，选第k个，但是代码超时了。
【思考】
全排列构成的多叉树的叶子结点有n!个，可以根据k在n!的位置进行剪枝，比如第二层的每个分支有(n-1)!个叶子结点。
所以如果k<(n-1)!就可以把其他分支的结点剪掉。

"""


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        超时的解法
        """
        used = [False for _ in range(n+1)]
        fac = [1 for _ in range(n+1)]
        for i in range(2, n+1):
            fac[i] = fac[i-1]*i

        def backtrack(pos, temp, k):
            if len(temp) == n:
                return
            # 回溯到pos层的时候，该pos层下的分支携带的叶子结点的数量是fac[n-pos-1]
            cnt = fac[n - pos - 1]

            # permutation每个位置都有n中选择，所以是range是0-n
            for index in range(1, n+1):

                if used[index]:
                    continue
                # 如果pos层该分支的结点的数量小于k的数量，说明k在右边的分支，所以这条分支剪掉，并继续下一个pos
                if cnt < k:
                    k -= cnt
                    continue

                temp.append(index)
                used[index] = True
                # 之前无法通过是因为pos+1写成index+1了，排列的问题还是pos+1的
                backtrack(pos+1, temp, k)
                # 这里不必再回溯，因为可以通过阶乘确定位置了
                # used[index] = False
                # temp.pop()
                return
        if n == 0:
            return ""
        temp = []
        backtrack(0, temp, k)
        return ''.join([str(i) for i in temp])


if __name__ == "__main__":
    s = Solution()
    n = 4
    k = 9
    print(s.getPermutation(n, k))
