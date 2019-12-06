#encoding=utf-8
# 问题描述：有N个job，每个job有对应的完成的时间和规定完成时间内没有完成的损失
# 求最小损失的job完成顺序，其中L是每个job的损失，T是每个job完成所需要的时间。

# 思路：考虑两种极端的情况
# 1）每个job完成花费的时间相同：按照损失从大到小排序，先完成损失大的，这样可以保证最后损失最小。
# 2）每个job没完成的损失相同：按照完成时间从小到大排序，先完成时间短的job，这样可以保证剩下的job数量少，从而损失最小。

# 解决：不能单纯的只考虑时间或者损失，需要考虑的是L/T比率的问题
import math
def printJobsequence(L, T):
    n = len(L)
    res = sorted([i for i in range(n)], key=lambda i: float(L[i])/T[i])
    print(res)



if __name__ == "__main__":
    L = [3, 1, 2, 4]
    T = [4, 1000, 2, 5]
    printJobsequence(L,T)
    print(float(3)/4)
