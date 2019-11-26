#encoding:utf-8

"""
这是一个骑士走棋盘的问题：
骑士可以向上下左右走，每次向一个方向走一步，另一个方向走两步，或者一个方向走
两步，另一个方向走一步。现在有一个8*8的棋盘，骑士需要走完棋盘中的每个格子，且
每个格子有且仅可以走一次。
"""
n = 8
def isSafe(x, y, board):
    # 可抵达的条件
    if (x>=0 and y>=0 and x<n and y<n and board[x][y]==-1):
        return True
    return False

def printSolution(board):
    for i in range(n):
        level_res = []
        for j in range(n):
            level_res.append(str(board[i][j]))
        print(' '.join(level_res))

def solveKT():
    # move_x = [1, -1, -2, -2, -1, 1, 2, 2]
    # move_y = [2, 2, 1, -1, -2, -2, -1, 1]
    # move_x 和 move_y会影响回溯找路的速度，下面的是经过测试最快能找到路径的，上面的就很慢
    move_x = [2, 1, -1, -2, -2, -1, 1, 2] 
    move_y = [1, 2, 2, 1, -1, -2, -2, -1] 

    init_x = 0
    init_y = 0
    board = [[-1 for i in range(n)] for j in range(n)]
    # 第0步所在的位置
    board[init_x][init_y] = 0
    # pos表示走的第pos步
    pos = 1
    if not solveKTUtil(init_x, init_y, board, move_x, move_y, pos):
        print('Solution does not exist.')
    else:
        printSolution(board)

def solveKTUtil(x, y, board, move_x, move_y, pos):
    # 走到最后一步的时候
    if pos == n**2:
        return True
    # range(8)是因为骑士下一步的选择有八种可能性
    for i in range(8):
        new_x = x+move_x[i]
        new_y = y+move_y[i]
        # 判断新的一步抵达的位置是否合法
        if isSafe(new_x, new_y, board):
            # 合法的情况下更新board为pos,并在此基础上进行下一步
            board[new_x][new_y] = pos
            # 如果下一步有解，那么return True
            if solveKTUtil(new_x, new_y, board, move_x, move_y, pos+1):
                return True
            # 回溯更新为-1
            board[new_x][new_y] = -1
    return False

if __name__ == "__main__":
    solveKT()

