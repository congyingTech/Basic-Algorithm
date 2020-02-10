# encoding:utf-8
"""
问题描述：
一个m*n的方阵，机器人可以上下左右的移动，但是机器人不能访问数位和值大于k的格子
比如k=10，机器人可以访问(50,50)格子，但是不能访问(50,49)因为5+0+4+9>10而5+0+5+0=10

解决方案：
回溯法解决

"""
class Solution(object):
    def getSum(self, index):
        # 得到数位之和
        sum_i = 0
        while index//10 != 0:
            sum_i+=index//10
        sum_i+= index%10
        return sum_i
         
    def isSafe(self, i, j, m, n, board):
        if  0<=i<m and 0<=j<n and board[i][j] == 0:
            return True
        return False

    def findGrid(self, init_i, init_j, m, n, k, board):
        # 下一步有上下左右四种可能性
        move_x = [1, -1, 0, 0]
        move_y = [0, 0, 1, -1]
        for i in range(4):
            new_i, new_j = init_i+move_x[i], init_j+move_y[i]
            res = self.getSum(new_i)+self.getSum(new_j) if new_j>=0 and new_i>=0 else 0
            # 如果下一步走的坐标是安全的，那么走下一步
            if self.isSafe(new_i, new_j, m, n, board) and res<=k:
                print("i:{},j:{} and sum is {}".format(new_i, new_j, res))
                board[new_i][new_j] = 1
                self.findGrid(new_i, new_j, m, n, k, board)
                    
    def findRobotFields(self, m, n, k):
        init_i = 0
        init_j = 0
        board = [[0]*n for _ in range(m)]
        if k>0:
            board[0][0] = 1
        self.findGrid(init_i, init_j, m, n, k, board)
        # board是机器人可以运动的范围
        print(board)

        


if __name__ == "__main__":
    s = Solution()
    m = 5
    n = 3
    k = 3
    s.findRobotFields(m, n, k)