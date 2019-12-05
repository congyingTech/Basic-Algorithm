#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2019-11-26 11:05
"""


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seen = set()  # Store indicies we have seen during our backtrack dfs
        answers = set()  # Store valid tile combinations
        self.backtrack(tiles, seen, answers, '')
        print(answers)
        return len(answers)  # Return the NUMBER of possible answers, not actual

    # Recursive Function
    def backtrack(self, tiles, seen, answers, curr):
        if curr != '' and curr not in answers:
            answers.add(curr)

        for index in range(len(tiles)):
            if index not in seen:
                seen.add(index)
                self.backtrack(tiles, seen, answers, curr + tiles[index])
                seen.remove(index)


if __name__ == '__main__':
    s = Solution()
    print(s.numTilePossibilities('AAB'))
