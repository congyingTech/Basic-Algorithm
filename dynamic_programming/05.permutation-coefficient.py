# encoding:utf-8
# 问题描述：求排列的数值
# 解决思路1：A(n,k) = n!/(n-k)!
# 解决思路2：动态规划——从n个有序序列中取k个，有几种取法。
# 两种情况，第一种k-1个数从n-1个中取，第n个数即取第k个数值；第二种k个数从n-1中取，
# A(n, k) = k * A(n-1, k-1) + A(n-1,k)  从下面的代码中可以看出这个公式是错误的！
# 不是很理解上面的公式，我的理解是A(n,k) = n*A(n-1,k-1) 即第一个有n种选择的权利

def solve1(n,k):
    res_n = 1
    res_k = 1
    for i in range(1, n+1):
        res_n *= i

    for i in range(1, n-k+1):
        res_k *= i
    print(res_n, res_k)
    print(res_n/res_k)

def solve2(n,k):
    A = [[0]*(k+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(min(k,i)+1):
            if j==0 or i==j:
                A[i][j] = 1
            else:
                A[i][j] = j*A[i-1][j-1] + A[i-1][j]
    print(A[n][k])

def solve3(n,k):
    A = [[0]*(k+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(min(k,i)+1):
            if j==0:
                A[i][j] = 1
            else:
                A[i][j] = i*A[i-1][j-1]
    print(A[n][k])

if __name__ == "__main__":
    n = 10
    k = 3
    solve1(n, k)
    solve2(n, k)
    solve3(n, k)
    


