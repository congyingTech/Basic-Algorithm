def searchXiaoha(step,startx,starty):
    '''
    Args:movexy-是走的方案右下左上的顺时针顺序
    AlSteps:1.


    :return:
    '''

    movexy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    if p==startx and q==starty:
        #print(step)
        global min
        if step < min:
            min = step
        return
    for k in range(4):
        newx = startx+movexy[k][0]
        newy = starty+movexy[k][1]
        if newx<0 or newx>4 or newy<0 or newy>3:
            continue
        if data[newx][newy]==0 and book[newx][newy]==0: #如果startx，starty没有被占
            book[newx][newy] = 1 #向右走，然后标记为1
            searchXiaoha(step+1,newx, newy) #走到下一步
            book[newx][newy] = 0
    return



if __name__ == '__main__':
    '''
    data=0 0 1 0
         0 0 0 0
         0 0 1 0
         0 1 0 0
         0 0 0 1
    小哈的位置在(3,2),起点在(0,0)
    '''

    data = [[0,0,1,0],[0,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]]
    p,q=3,2 #小哈的位置
    startx,starty = 0,0 #起点位置
    min = 20
    #book = [[0]*4]*5,发生浅拷贝
    book = [[0]*4 for i in range(5)]
    book[startx][starty] = 1 #起点已经去过，标记为1，不能再次经过
    print(book)
    searchXiaoha(0,startx, starty)
    print(min)