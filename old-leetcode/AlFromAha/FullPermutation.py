#-*-coding:utf-8-*-
#用dfs的方法递归求解全排列


#注意python中的main函数中的变量是全局变量

#step表示a作为容器的下标
def dfs(step):
    if step == len(data):
        print(a)
        return #返回到最近一次调用dfs的地方，将最后一个空间收回


    for i, item in enumerate(data): #遍历data逐渐存放
        if book[i] == 0: #如果book[i]为0，表示该格子空闲
            a[step] = item #表示a的第step个空间存储第i个data, a存储过后需要book标记一下
            book[i] = 1
            dfs(step + 1)  # 然后到下一个存储空间进行存放data
            book[i] = 0 #当到了最后一个存储空间的时候，要把数收回，进行新一轮的存放
    return


if __name__ == '__main__':
    data = [2,3,4,5]
    a=[0]*len(data) #用来存储全排列的每个数字
    book = len(data) * [0]  # 用来标记data是否已经放到了存储空间a中，book是一个全局变量
    dfs(0)

