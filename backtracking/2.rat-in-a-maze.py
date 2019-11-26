# encoding:utf-8
"""
这是一个小老鼠走迷宫的问题：
N*N的迷宫，迷宫里面0的地方是不能用的，1的地方是可以用的，小老鼠只能向前或者向下走，起点是(0,0)
终点是(N-1, N-1)，小老鼠要成功从起点到终点
"""
n = 4
def isSafe(x, y, board):
    if (x>=0 and y>=0 and x<n and y<n and board[x][y]!=0):
        return True
    return False

def printSolution(board):
    for i in range(n):
        level_res = []
        for j in range(n):
            level_res.append(str(board[i][j]))
        print(' '.join(level_res))

def solveMaze():
    init_x, init_y = 0,0
    board = [[1 for i in range(n)] for j in range(n)]
    board[0][1] = 0
    board[0][2] = 0
    board[0][3] = 0
    #board[1][2] = 0
    board[2][2] = 0
    board[2][0] = 0
    #board[2][3] = 0
    print('-----Maze-----')
    printSolution(board)
    move_x = [1,0]
    move_y = [0,1]
    pos = 1
    if not solveMazeUtil(init_x, init_y, board, move_x, move_y, pos):
        print("Rat cannot go out Maze!")
    else:
        print("-----Rat Route-----")
        printSolution(board)

def solveMazeUtil(x, y , board, move_x, move_y, pos):
    if x==3 and y==3:
        return True
    for i in range(2):
        new_x = x+move_x[i]
        new_y = y+move_y[i]
        if isSafe(new_x, new_y, board):
            board[new_x][new_y] = pos
            if solveMazeUtil(new_x, new_y, board, move_x, move_y, pos+1):
                return True
            board[new_x][new_y] = 1
    return False
            

if __name__ == "__main__":
    solveMaze()