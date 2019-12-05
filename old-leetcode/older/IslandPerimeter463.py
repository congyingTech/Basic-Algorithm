class Solution(object):
    #观察得到：看上下左右是否为1，按1的个数减去边数
    def islandPerimeter(self, grid):
        m = len(grid)
        n = len(grid[0])
        sum = 0
        sub_sum = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sum += 1
                    #左边的
                    if j >= 1 and grid[i][j-1] == 1:
                        sub_sum += 1
                    #右边的
                    if j <= n-2 and grid[i][j+1] == 1:
                        sub_sum += 1
                    #上边的
                    if i >= 1 and grid[i-1][j] == 1:
                        sub_sum += 1
                    #下边的
                    if i<= m-2 and grid[i+1][j] == 1:
                        sub_sum += 1
        return sum*4 - sub_sum
                    
        

if __name__ == '__main__':
    grid = [[0,1,0,0],
            [1,1,1,1],
            [0,1,0,0],
            [1,1,0,0]]
    print(Solution().islandPerimeter(grid))
