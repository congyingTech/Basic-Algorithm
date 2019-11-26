#coding:utf-8

class Solution(object):
    # 超时
    def judge(self, num):
        n_sqr = int((num+0.5)**0.5)
        for i in range(2, n_sqr+1):
            if num%i == 0:
                #print("{} is not a prime num".format(num))
                return 

        return num

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = []
        for num in range(1, n):
            n = self.judge(num)
            if n and n!=1:
                res.append(n)
        return len(res)

class Solution1(object):
    
    def countPrimes(self, n):
        """
        根据sieve of Eratosthenes 筛选出素数
        """
        if n<3:
            return 0
        n_sqrt  = int((n+0.5)**0.5)
        res = [True]*n
        res[0:2] = [False]*len(res[0:2])
        for i in range(2, n_sqrt+1):
            res[i**2::i] = [False]*len(res[i**2::i])
        print(sum(res))

if __name__ == "__main__":
    
    s = Solution1()
    s.countPrimes(4)