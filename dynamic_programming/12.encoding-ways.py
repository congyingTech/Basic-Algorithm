# encoding:utf-8
# 问题描述：A～Z对应着0～25，给定一个数字字符串，求这个字符串对应几种字母编辑方式，
# 例如：0219可以是ACBJ或者ACX或者AZJ，三种编码方式
# 解决方案：
# 利用动态规划，状态dp[n]表示遍历第n个数字时，有多少种编码方式，对于第n个数字，无非是有：
# 1）第n个数字独立编码，那么dp[n] = dp[n-1]
# 2）第n个数字和前一个数字组合编码，如果和前一个数字的组合小于26，那么dp[n]=dp[n-2]
# 所以dp[n] = dp[n-1] + dp[n-2] if 10*item[n-1]+item[n]<26
# dp[n] = dp[n-1] if 10*item[n-1]+item[n]>=26
# 边界条件n=0时，dp[0]=1,n=1时，dp[1]=1或2

class Solution(object):
    def encodingWays(self,a):
        a = list(a)
        n = len(a)
        table = [0]*(n)
        table[0] = 1

        if int(a[0])<=0 or 10*int(a[0])+int(a[1])>=26:
            table[1] = 1
        else:
            table[1] = 2
        for i in range(2, n):
            if 10*int(a[i-1])+int(a[i])<26 and a[i-1]!=0:
                table[i] = table[i-2]+table[i-1]
            else:
                table[i] = table[i-1]
        print(table)
        print(table[-1])

if __name__ == "__main__":
    a = '1259'
    s = Solution()
    s.encodingWays(a)
