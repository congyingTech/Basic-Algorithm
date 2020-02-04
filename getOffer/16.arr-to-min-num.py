# encoding:utf-8
"""
问题描述：
给定一个数组，返回数组组成的最小的数字，比如[3,32,321]组成的最小的数是321323
解决方案：
1）给出数组所有数的全排列，然后找出来最小的那种
2）先将整数数组转为字符串数组，然后用比较器实现字符串比较大小。如果有字符串A和B， A + B < B + A，则A在前；反之B在前。最后将字符串数组连接去除返回值左侧的0。
"""

class Solution(object):
    def arr2minNum(self, arr):
        arr_str = list(map(str, arr))
        arr_str.sort(cmp=lambda x,y:(int(x+y)) - (int(y+x)))
        return ''.join(arr_str)
        

if __name__ == "__main__":
    s = Solution()
    arr = [3, 32, 321]
    print(s.arr2minNum(arr))