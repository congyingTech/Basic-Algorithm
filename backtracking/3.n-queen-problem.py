#encoding:utf-8
n=8
k=4

def invalid_coord(x,y):
    x_list = [(x,i) for i in range(n)]
    y_list = [(i,y) for i in range(n)]
    # 左上角
    diag1 = [(x-i,y-i) for i in range(min(x,y)+1)]
    # 右上角
    diag2 = [(x-i,y+i) for i in range(min(x, n-y-1)+1)]
    # 左下角
    diag3 = [(x+i,y-i) for i in range(min(y,n-x-1)+1)]
    # 右下角
    diag4 = [(x+i,y+i) for i in range(min(n-x-1, n-y-1)+1)]
    invalid_coord = list(set(x_list+y_list+diag1+diag2+diag3+diag4))
    return invalid_coord

def isSafe(x, y, board):
    invalid_coords = invalid_coord(x,y)
    for coord in invalid_coords:
        x,y = coord
        if board[x][y]!=0:
            return False
    if board[x][y] != 0 and (x>n-1 or y>n-1): 
        return False
    return True

def printSolution(board):
    for i in range(n):
        level_res = []
        for j in range(n):
            level_res.append(str(board[i][j]))
        print(' '.join(level_res))

def solveQueen():
    board = [[0 for i in range(n)] for j in range(n)]
    init_x = 0
    init_y = 3
    board[init_x][init_y]=1
    pos = 1
    temp = []
    possible_x_y = [(i,j) for i in range(n) for j in range(n)]
    if solveQueenUtil(init_x, init_y, pos, board, possible_x_y, temp):
        printSolution(board)
    else:
        print("No result!")

def solveQueenUtil(x, y, pos, board, possible_x_y, temp):
    # 终止条件
    if pos == k:
        return True
    all_possible = [(i,j) for i in range(n) for j in range(n)]
    possible_x_y = list(set(all_possible) - set(invalid_coord(x,y))-set(temp))
    # for循环就是每次遍历下一步所有的可能
    for coord in possible_x_y:
        new_x, new_y = coord
        if isSafe(new_x,new_y,board):
            board[new_x][new_y] = pos
            temp.append((new_x, new_y))
            if solveQueenUtil(new_x,new_y,pos+1, board, possible_x_y, temp):
                return True
            board[new_x][new_y] = 0
            temp.pop()
    return False

if __name__ == "__main__":
    #board = [[1 for i in range(n)] for j in range(n)]
    solveQueen()
    