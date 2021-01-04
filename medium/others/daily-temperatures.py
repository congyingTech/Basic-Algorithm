# encoding:utf-8
"""
问题描述：
给定一组temperatures，寻找
解决方案：
"""
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        sta = []
        T_n = len(T)
        ans = [0]*T_n
        for i in range(T_n-1, -1, -1):
            while sta and T[i]>=T[sta[-1]]:
                sta.pop()
            if sta:    
                ans[i] = sta[-1]-i
            sta.append(i)
        return ans

if __name__ == "__main__":
    s = Solution()
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(s.dailyTemperatures(T))