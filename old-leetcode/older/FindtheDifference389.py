class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_l = list(s)
        s_t = list(t)
        ss_l = sum([ord(i)for i in s_l])
        ss_t = sum([ord(i)for i in s_t])
        return chr(ss_t-ss_l)

if __name__ == "__main__":
    ss = Solution()
    s = "abcd"
    t = "eacbd"
    print(ss.findTheDifference(s, t))
