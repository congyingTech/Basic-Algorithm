"""
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 

示例 1:

输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
示例 2:

输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change-2

思路：
dp[amount]表示总和是amount的硬币的组合数
dp[amount] = 求和dp[amount-ci] ci in coins
组合数外层for循环是物品列表，内层for循环是背包
"""


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for value in range(coin, amount+1):
                dp[value] += dp[value-coin]
        return dp[amount]


if __name__ == "__main__":
    s = Solution()
    amount = 5
    coins = [1, 2, 5]
    print(s.change(amount, coins))
