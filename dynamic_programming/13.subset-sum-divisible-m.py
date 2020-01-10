# encoding:utf-8
# 问题描述：子集的和是否可以被m整除
# exp:Input : arr[] = {3, 1, 7, 5};
#     m = 6;
#     Output : YES

# 解决方案：对于第n个数，无非是参与或不参与组成被6整除的sum：dp[n,sum]表示第n个数且和为sum时，子集的和是否被6除的状态
# 1）参与：dp[n,sum] = dp[n-1, sum-arr[n]]
# 2）不参与：dp[n, sum] = dp[n-1, sum]
# 边界条件：n==0，且sum>0时dp[0,sum]=False; sum==0，dp[n,0]=True
# 简而言之，就是subset-sum-problem的变种

class Solution(object):
    def solve(self, arr, m):
        n = len(arr)
        temp = int(sum(arr)/m)
        m = temp*m
        ans = [m*i for i in range(1, temp+1)]
        table = [[False]*(m+1) for i in range(n+1)]
        for i in range(n+1):
            table[i][0]=True

        for i in range(1, n+1):
            for j in range(1, m+1):
                if j-arr[i-1]>=0:
                    table[i][j] = table[i-1][j] or table[i-1][j-arr[i-1]]
                else:
                    table[i][j] = table[i-1][j]    

        for i in ans:
            if table[n][i] == True:
                print('Yes')
            else:
                print('No')

if __name__ == "__main__":
    s = Solution()
    arr = [1,6]
    m = 5
    s.solve(arr, m)