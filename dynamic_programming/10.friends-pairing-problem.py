# encoding:utf-8
# 问题描述：给定n个朋友，每个人可以保持单身，也可以与其他朋友配对。每个朋友只能配对一次。找出让朋友保持单身或配对的方式总数。
# Input  : n = 3
# Output : 4
# Explanation
# {1}, {2}, {3} : all single
# {1}, {2, 3} : 2 and 3 paired but 1 is single.
# {1, 2}, {3} : 1 and 2 are paired but 3 is single.
# {1, 3}, {2} : 1 and 3 are paired but 2 is single.
# Note that {1, 2} and {2, 1} are considered same.

# 解决方案：状态f(n)表示第n个人的时候，有多少种方式，每一个人有两种选择
# 1)保持单身，这样f(n)=f(n-1) 
# 2)跟其他的n个人配对，这样需要n个人需要预留出来2个人能够配对，除了第n个人，另一个人从其他n-1个人种随意挑选
# f(n) = (n-1)*f(n-2)
# 所以状态转移方程有：f(n) = f(n-1) + (n-1)*f(n-2)
# 边界条件：n<0时=0，n==0时=1

class Solution(object):

    def friends_pairing_problem(self, n):
        """
        递归的方法解决
        """
        if n<=2:
            return n
        
        return self.friends_pairing_problem(n-1) + (n-1)*self.friends_pairing_problem(n-2)


class Solution1(object):
    def friends_pairing_problem(self, n):
        """
        自底向上的递归法
        """
        ans = [0]*(n+1)
        ans[0] = 0
        ans[1] = 1
        ans[2] = 2
        for i in range(3, n+1):
            ans[i] = ans[i-1] + (i-1)*ans[i-2]
        print(ans)
        return ans[-1]

    



if __name__ == "__main__":
    n = 10
    s = Solution()
    res = s.friends_pairing_problem(n)
    print(res)
    s1 = Solution1()
    print(s1.friends_pairing_problem(n))
