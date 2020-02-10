# encoding:utf-8
"""
问题描述：
我们把只包含因子2，3，5的数称作丑数
解决方案：
1)暴力找到第1500个丑数，时间复杂度过高
2）用空间换时间，上面之所以慢，是因为要一个个的判断是不是丑数，可以通过将丑数保存起来，在丑数的基础上乘以，2，3，5来只寻找丑数
原理：因为丑数只包含质因子2，3，5，假设我们已经有n-1个丑数，按照顺序排列，且第n-1的丑数为M。那么第n个丑数一定是由这n-1个丑数分别乘以2，3，5，得到的所有大于M的结果中，最小的那个数。
事实上我们不需要每次都计算前面所有丑数乘以2，3，5的结果，然后再比较大小。因为在已存在的丑数中，一定存在某个数T2，在它之前的所有数乘以2都小于已有丑数，而T2×2的结果一定大于M，同理，也存在这样的数T3，T5，我们只需要标记这三个数即可。

"""
class Solution2(object):
    def findUglyNum(self, k):
        if k == 0:
            return 0
        ugly_list = [1]
        min2, min3, min5 = 0, 0, 0 
        i = 1 # 从坐标为1的丑数开始，也就是第二个丑数
        while i < k: 
            minnum = min([ugly_list[min2]*2, ugly_list[min3]*3, ugly_list[min5]*5])
            ugly_list.append(minnum)
            # 寻找T2，T3，T5的坐标
            while ugly_list[min2]*2 <= minnum:
                min2 += 1
            while ugly_list[min3]*3 <= minnum:
                min3 += 1
            while ugly_list[min5]*5 <= minnum:
                min5 += 1
            i+=1
        print(ugly_list[-1])

class Solution1(object):
    def findUglyNum(self, k):
        num=1
        while k>0:
            if self.isUgly(num):
                k-=1
            num+=1
        else:
            print(num)
        
    def isUgly(self, num):
        while num%2==0:
            num = num/2
        while num%3==0:
            num = num/3
        while num%5==0:
            num = num/5
        return num==1

if __name__ == "__main__":
    s = Solution2()
    k = 20
    s.findUglyNum(k)