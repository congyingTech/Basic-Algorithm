#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2019-06-21 16:04
"""

"""
M个台阶，每个台阶能吃bi个虫子，每次能上1，2步，最多能走N步，问最多吃多少？

定义状态：i, j , i是第i个台阶， j是第j步数


最优子结构：F(i, j) = max(F(i-1, j-1), F(i-2, j-1)) + b[i] 其中j<=M, i<=N
"""

import numpy as np


def max_sum(M, N, b):
    """
    :param M: M步数
    :param N: N个台阶
    :param b: bugs
    :return:
    """
    if M <= 0 or N <= 0:
        return 0
    res = np.array([[None] * N for _ in range(M)])
    res[0][0] = b[0]
    res[0][1] = b[1]
    for m in range(1, M):
        for n in range(1, N):
            if res[m - 1][n - 2] and res[m - 1][n - 1]:
                res[m][n] = max(res[m - 1][n - 2], res[m - 1][n - 1]) + b[n]
            elif res[m - 1][n - 1]:
                a = res[m - 1][n - 1]
                res[m][n] = a + b[n]
            elif res[m - 1][n - 2]:
                a = res[m - 1][n - 2]
                res[m][n] = a + b[n]
    print(max([i for i in res[M - 1][:] if i]))


def getMax(Bugs, m, start):
    """
    :type Bugs: List[int], the list of bugs
    :type m: int, number of jumps
    :type start: int, starting position

    """
    if m <= 0:
        return 0
    if m >= len(Bugs) - 1 - start:
        return (sum(Bugs[start + 1:]))
    if start + 2 < len(Bugs):
        candidate1 = Bugs[start + 2] + getMax(Bugs, m - 1, start + 2)
        candidate2 = Bugs[start + 1] + getMax(Bugs, m - 1, start + 1)
    elif start + 1 < len(Bugs):
        candidate1 = 0
        candidate2 = Bugs[start + 1] + getMax(Bugs, m - 1, start + 1)
    else:
        candidate1 = 0
        candidate2 = 0
    return max(candidate1, candidate2)


if __name__ == "__main__":
    b = [3, 1, 3, 5, 4]
    N = 5
    M = 3
    max_sum(M, N, b)
    a = getMax(b, M, -1)
    print(a)

