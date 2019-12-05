import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        sqrtval = int(math.sqrt(area))
        #从sqrtval到0的递减遍历
        for i in range(sqrtval, 0 ,-1):
            if area % i == 0:
                L, W = int(area/i), i
                break
        return(L,W)

if __name__ == "__main__":
    s = Solution()
    area = 6
    print(s.constructRectangle(area))
