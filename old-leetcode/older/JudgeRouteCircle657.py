#-*-coding:utf-8-*-
class Solution(object):
#虽然通过了，但是效率极低，还是要善于用count啊,
#return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        moves_l = list(moves)
        flag_u = 1
        flag_d = -1
        flag_l = 2
        flag_r = -2
        sum = 0
        for e in moves_l:
            if e == 'U':
                sum += flag_u
            if e == 'D':
                sum += flag_d
            if e == 'L':
                sum += flag_l
            if e == 'R':
                sum += flag_r
        if sum == 0:
            return True
        return False
if __name__ == "__main__":
    s = Solution()
    print(s.judgeCircle("LR"))