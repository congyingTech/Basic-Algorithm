class Solution(object):
    def convertToTitle(self, num):
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:  # num-1是因为capitals是从0下标开始的
            result.append(capitals[(num-1)%26])
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)
  

if __name__ == "__main__":
    s = Solution()
    n = 111
    s.convertToTitle(n)