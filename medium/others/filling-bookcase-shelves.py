#encoding:utf-8

class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        状态定义：dp是代表在放置的前i本书的最小的高度
        递推公式：到第i+1本书有两种摆放的情况:
        第一种是这本书单独是一层，那么dp[i+1] = dp[i]+books[i+1][1]
        第二种是这本书和别的书一起在一层，那么假设从j+1到i+1是在一层，
        dp[i+1] = dp[j]+max(books[j+1][1]~books[i+1][1] )))
        从两种情况取min
        约束条件是sum(books[j+1][0]~books[i+1][0])<=shelf_width
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        n = len(books)
        dp = [float('inf') for _ in range(n+1)]
        dp[0]=0
        for i in range(1, n+1):
            w = books[i-1][0]
            h = books[i-1][1]
            dp[i] = dp[i-1]+h # 这一步是直接把第i-1个作为单独一层
            for j in range(i-1, 0, -1):
                w += books[j-1][0]
                h = max(h, books[j-1][1])
                if(w>shelf_width):
                    break
                dp[i]=min(dp[i], dp[j-1]+h)
        
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    books = [[1,3],[2,4],[3,2]]
    shelf_width = 6
    print(s.minHeightShelves(books, shelf_width))