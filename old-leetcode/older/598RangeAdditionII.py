class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops: return m * n
        x = []
        y = []
        for e in ops:
            x.append(e[0])
            y.append(e[1])
        xmin = min(x)
        ymin = min(y)
        return xmin*ymin
if __name__ == "__main__":
    s = Solution()
    m = 3
    n = 3
    operations = [[2,1],[3,3]]
    print(s.maxCount(m, n, operations))