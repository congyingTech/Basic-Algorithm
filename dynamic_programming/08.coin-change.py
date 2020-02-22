# encoding:utf-8
# 问题描述：假设S是硬币的面值的大小，N是找零的钱，找零的组合有几种？
# exp：S={1,2,3} N=4，那么{1,1,1,1} {2,2} {1,1,2} {1,3} 四种组合可以找零4

# 解决方案
# 回溯法：Solution

# 动态规划：Solution1
# count(N,m)表示凑成N且第m个元素被包括时，有多少种可能
# 假设m是S中第m个元素，对于元素m，组成N有两种方式:
# 1.至少包含一个第m个元素才能组成N，count(N-Sm, m)
# 2.不包含m个元素（即前m-1个元素）就能组成, count(N,m-1)
# count(N,m) = count(N-Sm,m) + count(N,m-1)


# 动态规划: Solution2
# 状态A[N]表示凑齐N的时候，有多少种方法？组成A[N]的有三种方式：
# 1.A[N-1]表示最后一步用1硬币凑N,那么A[N-1]是前面凑齐N-1的方法数
# 2.A[N-2]表示最后一步用2硬币凑N，那么N-2需要多少种方法
# 3.A[N-3]表示最后一步用3硬币凑
# A[N] += A[N-Si]


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        temp = []
        ans = []
        self.solve_backtrack(temp, coins, amount, ans)
        if not ans:
            return -1
        return len(ans)
        # min_len = len(ans[0])
        # for i in ans:
        #     if len(i)<=min_len:
        #         min_len = len(i)
        # return min_len

    def solve_backtrack(self, temp, S, N, ans):
        # 超时的算法，太慢了，要遍历出来所有的组合可能，但是答案也是对的
        if sum(temp) == N and sorted(temp) not in ans:
            ans.append(temp[:])
            return
        for i in S:
            if sum(temp)<N :
                temp.append(i)
                self.solve_backtrack(temp, S, N, ans)
                temp.pop()
            else:
                return


class Solution1(object):
    def helper_inner(self, coins, m, amout):
        '''
        m是第m个硬币
        '''
        if amout<0:
            return 0
        if amout == 0:
            return 1
        if amout>=1 and m<=0:
            return 0

        return self.helper_inner(coins, m, amout-coins[m-1]) + self.helper_inner(coins, m-1, amout)

    def coinChange(self, coins, amout):
        m = len(coins)
        ans = self.helper_inner(coins,m, amout)
        print(ans)


class Solution2(object):

    def coinChange(self, coins, amout):
        res = [0] * (amout + 1)
        res[0] = 1
        for i in range(len(coins)):
            for j in range(S[i], amout+1):
                res[j] += res[j-coins[i]]
        return res[-1] 
        
if __name__ == "__main__":
    S=[1,2,3]
    N= 4
    s = Solution2()
    print(s.coinChange(S, N))

