class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ans = []
        lo, hi = 0, len(S)
        for s in S:
            if s=='I':
                ans.append(lo)
                lo+=1
            else:
                ans.append(hi)
                hi-=1
        return ans+[lo]
        

if __name__ == "__main__":
    S = 'IDIDDDDIDIIIDD'
    s = Solution()
    s.diStringMatch(S)