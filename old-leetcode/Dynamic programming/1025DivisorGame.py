#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2019-06-05 14:09
"""
'''
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.
'''


class Solution(object):
    res = []

    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        if N < 2:
            print('end here')
            return False
        x_list = [x for x in range(1, N) if N % x == 0]
        n = [N - x for x in x_list]
        print(x_list)
        for num in n:
            self.divisorGame(num)



if __name__ == "__main__":
    s = Solution()
    res = s.divisorGame(3)
    print(res)
