# encoding:utf-8

# 问题描述：input n=3,求对于{1，2，3}有多少中不同的分割方法
# 假设S(n,k)表示n的list，被分割成k个partition的方法数目
# 那么n个长度的list，可以分割的方法有S(n,0)+....S(n,k)+...S(n,n)
# 对于S(n,k)用动态规划的方法写出状态转移
# S(n,k)在k!=n和k!=1时有两种情况：
# 一种是第n个数当作独立的一个partition与S(n-1,k-1)组合，这样就有新的S(n-1,k-1)中
# 一种是第n个数当作数字插入到n-1个数目的list被分割成的k个的partition里面，
# S(n,k)在k=n和k=1时均为1

# 插入到k个partition里面，就有k*S(n-1, k)中组合
# 所以：S(n,k) = k*S(n-1, k) + S(n-1, k-1)


#PS:Bell Number就是n长度的list，总共有多少种分割法


def bellNumberFindPartitionWay(n):
    S = [[0]*(n+1) for i in range(n+1)]
    S[0][0] = 1

    for i in range(1, n+1):
        for k in range(1,i+1):
            if k==1 or i == k:
                S[i][k] = 1
            else:
                S[i][k] = k*S[i-1][k] + S[i-1][k-1]
    
    for i in range(n):
        print('Bell {} sum is:{}'.format(i, sum(S[i])))




if __name__ == "__main__":
    n = 10
    bellNumberFindPartitionWay(n)