class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        j = 0
        left = 0
        right = 0
        res = []
        for i in range(len(S)):
            if S[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                res.append(S[j+1: i])
                j = i + 1
        return "".join(res)

if __name__ == "__main__":
    s = Solution()
    print(s.removeOuterParentheses("((()))()(())"))