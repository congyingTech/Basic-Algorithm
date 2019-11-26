class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        a = address.replace('.', '[.]')
        return a

if __name__ == "__main__":
    s = Solution()
    res = s.defangIPaddr("1.1.1.1")
    print(res)