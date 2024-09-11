class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        n = len(s)
        temp = list()
        for i in range(n):
            right = i
            while right < n and s[right] not in temp:
                temp.append(s[right])
                right += 1
            ans = max(ans, len(temp))
            temp = list()
        return ans


if __name__ == "__main__":
    sol = Solution()
    s = 'aaaannnnnbbbbcks'
    sol.lengthOfLongestSubstring(s)
