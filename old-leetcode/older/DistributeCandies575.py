class Solution(object):
    def distributeCandies(self, candies):
        c_s = set(candies)
        if len(c_s) >= len(candies)/2:
            return int(len(candies)/2)
        else:
            return len(c_s)
if __name__ == '__main__':
    candies = [1,1,2,3,1,1]
    print(Solution().distributeCandies(candies))
