#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-18 00:09
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def check(i, j, k):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            if board[i][j] != word[k]:
                return False
            if k == len(word)-1:
                return True
            visited.add((i,j))
            result = False
            for gap_i, gap_j in directions:
                new_i, new_j = i+gap_i, j+gap_j
                if 0<=new_j<n and 0<=new_i<m:
                    if (new_i, new_j) not in visited:
                        if check(new_i, new_j, k+1):
                            result = True
                            break
            visited.remove((i,j))
            return result

        m = len(board)
        n = len(board[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                # 只要有一个i，j满足就可以return了
                if check(i, j, 0):
                    return True
        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(Solution().exist(board, word))
