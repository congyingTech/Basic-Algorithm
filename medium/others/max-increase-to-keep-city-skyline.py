#encoding:utf-8

# The grid is:
# [ [3, 0, 8, 4], 
#   [2, 4, 5, 7],
#   [9, 2, 6, 3],
#   [0, 3, 1, 0] ]

# gridNew = [ [8, 4, 8, 7],
#             [7, 4, 7, 7],
#             [9, 4, 8, 7],
#             [3, 3, 3, 3] ]

# gridNew的由来：gridNew x=0,y=0的计算是x行y列最大值中的最小值


class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #gridNew=[[0 for i in range(len(grid))] for j in range(len(grid[0]))]
        all_rows = []
        all_columns = []
        for i in range(len(grid)):
            rows = grid[i][:]
            all_rows.append(rows)
            columns = [grid[j][i] for j in range(len(grid[0]))]
            all_columns.append(columns)
            #print(rows, columns)
        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #print(min(max(all_rows[i]), max(all_columns[j])))
                tmp = min(max(all_rows[i]), max(all_columns[j]))
                #gridNew[i][j] = tmp
                sum += tmp-grid[i][j]
        #print(sum)
        return sum
        #print(gridNew)


    def maxIncreaseKeepingSkyline1(self, grid):
        """
        zip(*grid)可以方便的把矩阵转置
        """
        max_rows = [max(row) for row in grid]
        max_columns = [max(column) for column in zip(*grid)]
        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sum += min(max_rows[i], max_columns[j])-grid[i][j]
        return sum


if __name__ == "__main__":
    s = Solution()
    grid = [[3, 0, 8, 4], 
            [2, 4, 5, 7],
            [9, 2, 6, 3],
            [0, 3, 1, 0] ]
    res = s.maxIncreaseKeepingSkyline1(grid)
    print(res)