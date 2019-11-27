# encoding:utf-8

# 问题描述
# Egyptian Fraction Representation of 2/3 is 1/2 + 1/6
# Egyptian Fraction Representation of 6/14 is 1/3 + 1/11 + 1/231
# Egyptian Fraction Representation ofw 12/13 is 1/2 + 1/3 + 1/12 + 1/156
# 思路：求2/3的埃及数，ceil(3/2) = 2，那么第一个单元分数是1/2，
#     接着求（2/3-1/2=1/6），1/6本来就是单元分数了，所以停止
import math


def computeUnitFraction(num,res):

    if num == 0:
        return None
    a = math.ceil(1/num)
    print("1/{} is unit fraction".format(a))
    num = (num-1/a)
    res.append('1/{}'.format(a))
    computeUnitFraction(num,res)
    return res

if __name__ == "__main__":
    num = 11/13
    res = []
    res = computeUnitFraction(num, res)
    print(res[:-1])