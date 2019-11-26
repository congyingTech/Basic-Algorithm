class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count  = 0
        for i in S:
            if i in J:
                count += 1
                
        return count

if __name__ == "__main__":
    s = Solution()
    print(s.numJewelsInStones('aA', 'aAAsssss'))