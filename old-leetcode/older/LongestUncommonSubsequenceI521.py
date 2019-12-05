class Solution(object):
    def findLUSlength(self, a, b):
        if a==b:
            return -1
        return len(a) if len(a) > len(b) else len(b)
                


if __name__ == "__main__":
    a = "aba"
    b = "abaa"
    print(Solution().findLUSlength(a, b))