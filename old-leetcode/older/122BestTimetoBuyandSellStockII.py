class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return  sum([max(prices[i + 1] - prices[i], 0) for i in range(len(prices)-1)])
if __name__ == '__main__':
    s = Solution()
    prices = [3,1,4,1,2,3,0]
    print(s.maxProfit(prices))
