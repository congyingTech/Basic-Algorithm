# encoding:utf-8

class Solution(object):
    def permutation(self, str_n):
        str_l = list(str_n)
        n = len(str_l)
        temp = []
        self.backtracking(0, n, str_l, temp)
    

    def backtracking(self, index, n, str_l, temp):
        if len(temp) == n:
            print(temp)
        for i in range(n):
            if str_l[i] not in temp and index!=n:
                temp.append(str_l[i])
                self.backtracking(index+1, n, str_l, temp)
                temp.pop()

if __name__ == "__main__":
    s = Solution()
    a = 'abc'
    s.permutation(a)