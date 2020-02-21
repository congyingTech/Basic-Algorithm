# encoding:utf-8
# 问题描述：求解第n个丑数
# 解决方法：
# 1）传统方法； 
# 2）动态规划：自底向上构建
def maxDivide(a,b):
    while a%b == 0:
        a = a/b
    return a
def isUgly(no):
    no = maxDivide(no, 2)
    no = maxDivide(no, 3)
    no = maxDivide(no, 5)
    return 1 if no == 1 else 0   

def getNthUgly(n):
    i = 1
    count = 1
    while n>count:
        i+=1
        if isUgly(i):
            count += 1
    return i

def dpSolve(n):
    """
    时间空间复杂度都是O(N)
    动态规划的方法从底向上构建ugly list
    """
    ugly = [0]*n
    ugly[0] = 1
    i2 = i3 = i5 = 0
    for i in range(1, n):
        i2_res = ugly[i2]*2
        i3_res = ugly[i3]*3
        i5_res = ugly[i5]*5
        ugly[i] = min(i2_res, i3_res, i5_res)
        if ugly[i] == i2_res:
            i2 += 1
        if ugly[i] == i3_res:
            i3 += 1
        if ugly[i] == i5_res:
            i5 += 1
    print(ugly)
        

if __name__ == "__main__":
    n = 10
    print(getNthUgly(n))
    
    dpSolve(n)