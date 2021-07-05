"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。

示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change

解题思路：
硬币的数量是无限的决定了该问题是完全背包问题。

xi是面值为ci的硬币的数量，i是面值的下标
min(∑x(i))
约束条件：x(i)*c(i) <= S
dp[S]表示组成S金额的最少的硬币数
dp[S] = min(dp[S], dp[S-c(i)] + 1) 0<=i<3
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    s = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(s.coinChange(coins, amount))
