class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = []
        max_s = ''
        max_len = 0
        for i in s:
            if i not in max_s:
                temp.append(i)
                if len(max_s)<len(temp):
                    max_s = ''.join(temp)
                    if len(max_s)>max_len:
                        max_len = len(max_s)
            else:
                temp = [i]
                max_s = i
        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('dvdf'))