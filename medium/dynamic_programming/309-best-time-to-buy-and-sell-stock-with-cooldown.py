"""
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

解题思路：
dp的思想：
dp表示股票的最大收益，股票最大收益有三种状态，
首先，有股票就不可能处于冷冻期，因为只有卖出才会处于冷冻期，所以只有以下三种状态
0.手中有股票，dp[i][0]表示此状态下最大收益
1.手中无股票，且处于非冷冻期，dp[i][1]表示此状态下最大收益
2.手中无股票，且处于冷冻期，dp[i][2]表示此状态下最大收益，（这里的处于冷冻期指的是，i天结束之后的状态，也就是i天结束之后处于冷冻期，那么i+1天不能买股票）
三种状态的转移方程：
0.dp[i][0]可以由dp[i-1][0](前一天手中由股票状态)和dp[i-1][1](前一天手中无股票且处于非冷冻期)买入转化而来
dp[i][0] = max(dp[i-1][0], dp[i-1][1]-price[i])
1.dp[i][1]无股票且不处于冷冻期，说明第i天无任何操作,且i-1天无股票（因为有的话就会进入冷冻期），这个状态可以由前一天无股票且不处于冷冻期和前一天无股票但是处于冷冻期转化而来
dp[i][1] = max(dp[i-1][1], dp[i-1][2])
2.dp[i][2]无股票且冷冻期，一定是今天卖出了
dp[i][2] = dp[i-1][0]+price[i]

那么最终的最大收益就是max(dp[n-1][0], dp[n-1][1], dp[n-1][2])
时间复杂度O(N),空间复杂度O(N^2)


空间优化：f0 = dp[i][0], f1=dp[i][1], f2=dp[i][2]
空间复杂度为O(N)
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        dp = [[0]*3 for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][2])
            dp[i][2] = dp[i-1][0] + prices[i]

        return max(dp[n-1][0], dp[n-1][1], dp[n-1][2])


if __name__ == "__main__":
    s = Solution()
    prices = [1,2,3,0,2]
    print(s.maxProfit(prices))
