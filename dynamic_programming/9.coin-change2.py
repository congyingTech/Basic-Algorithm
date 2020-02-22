# encoding:utf-8
# 问题描述：假设S是硬币的面值的大小，N是找零的钱，找零的组合种用的硬币数量最少是多少个？
# exp：S={1,2,3} N=4，那么{1,1,1,1} {2,2} {1,1,2} {1,3} 四种组合可以找零硬币数量最少是2

# min_count[N,m]表示组合成N的第m个硬币的最小的硬币数，第m个硬币只能选或者不选。
# 选择第m个硬币min_count[N-Sm, m])+ 1
# 不选择硬币 min_count[N, m-1]
# 那么, min_count[N,m] = min(min_count[N-Sm, m])+ 1, min_count[N, m-1])
# 边界条件：N==0:return 0

 
class Solution_A(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        value1 = [0]
        value2 = []
        nc =  0
        visited = [False]*(amount+1)
        visited[0] = True
        while value1:
            nc += 1
            for v in value1:
                for coin in coins:
                    newval = v + coin
                    if newval == amount:
                        return nc
                    elif newval > amount:
                        continue
                    elif not visited[newval]:
                        visited[newval] = True
                        value2.append(newval)
            value1, value2 = value2, []
        return -1




class Solution(object):
    def coinChange(self, coins, amount):
        """
        递归的方法严重超时，改成动态规划
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        m = len(coins)
        if self.helper(coins, m, amount) == float('inf'):
            return -1
        else:
            return self.helper(coins, m, amount) 
    
    def helper(self, coins, m, amount):
        
        if amount<0:
            return float("inf")
        if amount == 0:
            return 0
        if amount>0 and m<0:
            return float("inf")
        
        return min(self.helper(coins, m, amount-coins[m-1])+1, self.helper(coins, m-1, amount))

class Solution1(object):
    def coinChange(self, coins, amount):
        m = len(coins)
        # m行，amount列,初始化
        table = [[float('inf')]*(amount+1) for i in range(m)]
        for i in range(m):
            table[i][0] = 0

        for i in range(m):
            for j in range(1,amount+1):
                if j>=coins[i]:
                    table[i][j] = min(table[i][j-coins[i]]+1,table[i-1][j])
                else:
                    table[i][j] = table[i-1][j]
        if table[m-1][amount] == float('inf'):
            return -1
        return table[m-1][amount]


if __name__ == "__main__":
    S=[1,4,7]
    N=118
    S = [3,7,405,436]
    N=883
    S = [1,2147483647]
    N = 2
    s_a = Solution_A()
    print('正确答案是:{}'.format(s_a.coinChange(S,N)))
    s = Solution()
    print('我的答案是:{}'.format(s.coinChange(S, N)))
    s1 = Solution1()
    print('我的答案是:{}'.format(s1.coinChange(S, N)))
