# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 2:59 下午
# @Author  : Mohn
# @FileName: meituan.py


def findMaxSum(nums):
    max_res = 0
    for i in range(len(nums)):
        max_res += nums[i]
        if max_res < 0:
            max_res = 0
    return max_res


if __name__ == "__main__":
    nums = [1, -5, 2, 3, -4, 5, 8]
    print(findMaxSum(nums))

