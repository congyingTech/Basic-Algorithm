# encoding: utf-8
"""
问题描述：
把n个骰子扔在地上，所有骰子的点数一定会产生一个和值，假设所有骰子朝上一面的点数之和是s，
输入n，打印出s的所有可能值出现的概率。
解决方案：
骰子的大小是从1～6，那么n个骰子的最小的和值是n，最大的和值是6n
那么定义一个长度是6n-n+1的数组保存点数和为s出现的次数。和为s的点数保存在s-n个元素里。
1）递归的思路：n个元素组成s，那么分为两堆，一堆是第n个骰子，另一堆是n-1个骰子，那么f(n, s)代表第n个元素组成s的可能的个数
第n个可能取值是1～6，那么前n-1个对应的取值是s-1～s-6
f(n, s) = f(n-1, s-1) + f(n-1, s-2) + f(n-1, s-2) + f(n-1, s-3) + .....f(n-1, s-6)

但是递归的问题是太慢了，当n越大的时候，非常容易超时

2)用时间换空间，用数组的方法记录之前遍历过的数据（跟动态规划类似）
"""
class Solution(object):
    def findNProbability(self, n):
        res = []
        for s in range(n, 6*n+1):
            res.append(self.numberCount(n, s))
        return [(num/6**n)*100 for num in res]
    
    def numberCount(self, n, s):
        if n < 1 or s < n or s > 6 * n: return 0
        if n == 1: return 1
        
        count = self.numberCount(n-1, s-1) + self.numberCount(n-1, s-2) + \
                self.numberCount(n-1, s-3) + self.numberCount(n-1, s-4) + \
                self.numberCount(n-1, s-5) + self.numberCount(n-1, s-6)
        return count

class Solution1(object):
    def findNProbability(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # 为了将index与n对应上，特意把第0行空出来
        res = [[0 for i in range(6*n+1)] for i in range(n+1)]
        
        # 将第0行与第0列空出来，res[1][1:7] = [1,1,1,1,1,1]
        # 表示第一个骰子6种情况各出现一次
        for i in range(1,7):
            res[1][i] = 1
        
        # 从第二个骰子开始遍历
        for i in range(2,n+1):
        	# n个骰子之和的范围为n到6*n
            for j in range(i, 6*i+1):
            	# 当 j > 6 时，f(n) = f(n-1) +f(n-2) f(n-3)+ f(n-4) +f(n-5)+ f(n-6)
            	# 当 j <= 6 时，例如3，f(n) = f(n-1) +f(n-2)
                for k in range(1, min(j+1,7)):
                    res[i][j] += res[i-1][j-k]
        
        return res[-1][n:]




if __name__ == "__main__":
    s = Solution()
    n = 3
    print(s.findNProbability(n))