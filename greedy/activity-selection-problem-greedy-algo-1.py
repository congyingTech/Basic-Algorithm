# encoding:utf-8
# 求最大的活动数
# 先对f进行从小到大的排序，然后i是start的下标，j是finish的下标，如果后一个start的时间大于等于前一个finish的时间
# 那么后一个活动可以加入！

def solveMaxActivities(s,f):
    n = len(s)
    print('activity 0 is selected!')
    i = 0 # start的下标
    for j in range(1, n):
        if s[j]>=f[i]:
            print('activity {} is selected!'.format(j))
            i = j

if __name__ == "__main__":
    #s = [1 , 3 , 0 , 5 , 8 , 5] 
    #f = [2 , 4 , 6 , 7 , 9 , 9] 
    # s,f中f是无序的
    s = [3, 0, 1, 5, 8, 5]
    f = [4, 6, 2, 7, 9, 9]
    sorted_index = sorted(range(len(f)), key=lambda x: f[x])
    sorted_s = [s[i] for i in sorted_index]
    sorted_f = [f[i] for i in sorted_index]

    solveMaxActivities(sorted_s, sorted_f)