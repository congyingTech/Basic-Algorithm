# encoding:utf-8
# 问题：求解二项式系数，二项式系数就是组合数
# 二项式的展开公式:(a+b)^n = C(n,0)*a^n + ...C(n,k)*a^(n-k)*b^k...+ C(n,n)*b^n
# 二项式的系数就是组合数
# 组合数——从n个元素里面取k个元素
# 解法1:求排列组合数（排列是有序的，组合是无序的）
# 排列数（从n个不同元素中，任意取m个元素按一定的顺序排成一列，有多少种排列的组合，这样叫做排列数）：A(n,k) = (n)!/(n-k)!
# 组合数（从n个不同元素中，任意取m个元素拼成一组，有多少种可能的组合，这样叫做组合数）：C(n,k) = (n)!/k!(n-k)!

# 解法2:根据帕斯卡公式：
# (i)在第n个数时，第k个元素被拿出，此时方案数即从n-1个元素中拿了k-1个元素的方案数.
# (ii)在第n个数时，第k个元素没被拿出，此时方案即从n-1个元素中拿了k个元素的方案数.
# C(n,k) = C(n-1, k-1) + C(n-1, k)

from timeit import default_timer as timer

def solve1(n, k):
    if n == 0 or k==0:
        print(1)
        return
    n_res = 1
    for i in range(k):
        n_res *= n 
        n = n-1
    k_res = 1
    for i in range(k, 0, -1):
        k_res *= i
    print(n_res/k_res)

# 制表法-自底向上:[[1, 0, 0], [1, 1, 0], [1, 2, 1], [1, 3, 3], [1, 4, 6], [1, 5, 10]]
# 挨个的存储，状态直接找寻，比下面的更快，但是代码也更复杂
def solve2(n, k):
    C = [[0]*(k+1) for i in range(n+1)]
    #C[0][0] = 1
    #C[1][0] = 1
    for i in range(n+1):
        # min(i,k)是因为k永远小于等于n，所以求最小
        for j in range(min(i,k)+1):
            if j==i or j==0:
                C[i][j] = 1
            else: 
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    print(C)
    print(C[n][k])

# 记忆法-自顶向下:[[0, 0, 0], [0, 0, 0], [0, 2, 0], [0, 3, 3], [0, 4, 6], [0, 0, 10]]
# 只存储了需要的数据，但是还是有大量的递归
def solve3(n, k):
    mer =[[0]*(k+1) for i in range(n+1)]
    def inner_solve3(n, k):
        if k>n:
            return
        if k == 0 or k==n:
            return 1
        if not mer[n][k]:
            mer[n][k] = inner_solve3(n-1, k-1) + inner_solve3(n-1, k)
        return mer[n][k]    
    inner_solve3(n,k)
    print(mer)
    print(mer[n][k])


if __name__ == "__main__":
    n = 5
    k = 2
    start1 = timer()
    solve1(n,k)
    end1 = timer()
    print('Solve1 waste time:{}'.format(end1-start1))

    start2 = timer()
    solve2(n,k)
    end2 = timer()
    print('Solve2 waste time:{}'.format(end2-start2))

    start3 = timer()
    solve3(n,k)
    end3 = timer()
    print('Solve3 waste time:{}'.format(end3-start3))
