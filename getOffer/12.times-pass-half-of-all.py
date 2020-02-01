# encoding:utf-8
"""
问题描述：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如：输入[1,2,3,2,2,2,5,4,2]
解决方案：
1）快排的方法找到中位数
2）摩尔投票
数组中有一个数字出现的次数超过数组长度的一半，也就是说它出现的次数比其他所有数字出现次数的和还要多。
因此我们可以考虑在遍历数组的时候保存两个值：一个是数组的一个数字，一个是次数。
当我们遍历到下一个数字的时候，如果下一个数字和我们之前保存的数字相同，则次数加1；
如果下一个数字和我们之前保存的数字不同，则次数减1。
如果次数为零，我们需要保存下一个数字，并把次数设为1。
由于我们要找的数字出现的次数比其他所有数字出现的次数之和还要多，
那么要找的数字肯定是最后一次把次数设为1时对应的数字。

reference：https://blog.csdn.net/weixin_40314385/article/details/89578351
"""

class Solution(object):
    def findNumber(self, arr):
        times = 1
        number = arr[0]
        for num in arr:
            if times == 0:
                number = num
                times = 1
            elif num == number:
                times+=1
            else:
                times-=1

        if self.checkOutHalfNumber(arr, number):
            print(number)
            return number
            
        else:
            return 0

    def checkOutHalfNumber(self, arr, number):
        count = 0 
        for num in arr:
            if num == number:
                count += 1
        if count*2>=len(arr):
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    arr = [1,2,3,4,2]
    s.findNumber(arr)
