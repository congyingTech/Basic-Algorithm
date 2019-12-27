# encoding:utf-8
# 问题描述：n*m大小的矿，矿里的每个坑都有一个整数，是该矿坑包含的黄金量
# 最初一个矿工必须在第一列，但是可以在任意行，但是这个矿工只能朝着右边/右上/右下三个方向走，
# 问矿工能够收集的最大的黄金量？
# 解决方案：每一步有三种走向可能，状态dp[i][j]表示i行j列的最大黄金量,w[i][j]是该位置的黄金量
# dp[i+1][j-1]表示这一步是从上一步向右上走，dp[i][j-1]表示这一步是从上一步向右走，
# dp[i-1][j-1]表示这一步是从上一步的右下走过来的
# 状态转移公式是：dp[i][j] = max(dp[i+1][j-1], dp[i][j-1], dp[i-1][j-1]) + w[i][j]
# 边界条件：当i=n-1在最后一行时，前一个点只可能时从左上和左边过来，当i=0在第一行时，只能从左下或左边
# 过来，当j=0时，只能是开始被gold充满，当j=m-1最后一列时，表示已经结束。


def solve(n, m, gold):
    maxGold  = [[0]*m for i in range(n)]
    # 第一列被gold的第一列填充
    # i是行，j是列，n行m列
    for j in range(m):
        
        for i in range(n):
            if j==0:
                maxGold[i][j] = gold[i][0]
            elif i==0 and j!=0:
                maxGold[i][j] = max(maxGold[i][j-1], maxGold[i+1][j-1]) + gold[i][j]
            elif i==n-1 and j!=0:
                maxGold[i][j] = max(maxGold[i][j-1], maxGold[i-1][j-1]) + gold[i][j]                
            else:
                maxGold[i][j] = max(maxGold[i+1][j-1], maxGold[i][j-1], maxGold[i-1][j-1]) + gold[i][j]
    print(maxGold)

if __name__ == "__main__":
    gold = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    n = 5
    m = 3
   

    solve(n, m, gold)