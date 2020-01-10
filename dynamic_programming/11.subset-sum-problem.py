# encoding:utf-8
# 问题描述：
# 给定一组非负整数，和一个和值，求问能等于和值的数组子集组合是否存在
# 例如2, 3, 4, 5, 12, 34；9是和值；那么返回True
# 解决方案：状态dp[n,sum]表示第n个数加入且和为sum的状态(True or False)，对于第n个数只有参与或不参与组成sum：
# 1）如果前n-1个数已经和为sum了，那么第n个数不包括的情况下也是True
# 2）如果前n-1个数的和值为sum-set[n]，那么第n个数包括的情况下也是True
# 所以 dp[n, sum] = dp[n-1, sum] || dp[n-1, sum-set[n]]
# 边界条件sum==0时，dp[n, 0]=True; sum>0且n=0时，dp[0,sum]=False

class Solution(object):
    def isSubSetsum(self, l, sum_ans):
        n = len(l)
        table = [[False]*(sum_ans+1) for _ in range(n+1)]
        for i in range(n+1):
            table[i][0] = True
        
        for i in range(1, n+1):
            for j in range(1, sum_ans+1):
                if j-l[i-1]>=0:
                    table[i][j] = table[i-1][j] or table[i-1][j-l[i-1]]
                else:
                    table[i][j] = table[i-1][j]                    
        
        print(table)
        for i in range(n+1):
            if table[i][-1]==True:
                print(True)

class Solution1(object):
    """
    空间为O(N)
    """
    def isSubSetsum(self, l, sum_ans):
        pass


if __name__ == "__main__":
    l = [2, 3, 4, 12, 34]
    sum_ans = 8
    s = Solution()
    s.isSubSetsum(l, sum_ans)