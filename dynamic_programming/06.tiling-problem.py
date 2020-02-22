# encoding:utf-8
# 问题描述：2*n大小的空白地板，被2*1大小的地板砖填充满，问有多少种填充方式？
# 解决方法：对于第n块瓷砖，有水平放置和垂直放置两种可能：
# 1）如果第n块瓷砖水平放置，那么第二块瓷砖必然也要水平放置，所以看n-2块瓷砖的个数
# 2）如果第n块瓷砖垂直放置，那么看n-1块瓷砖的个数
# 所以dp[n]是n块瓷砖的摆放的个数，状态转移方程是：dp[n] = dp[n-1] + dp[n-2]

def solve1(n):
    tiles = [0] * (n+1)
    for i in range(1, n+1):
        if i==1 or i==2:
            tiles[i] = i
        else:
            tiles[i] = tiles[i-1] + tiles[i-2]
    print(tiles)
    print(tiles[n])

if __name__ == "__main__":
    n = 4
    solve1(n)
