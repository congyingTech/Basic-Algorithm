# encoding:utf-8
# ABC = [[], [A], [B], [C], [A,B], [A,C], [B,C], [A,B,C]]
"""
用回溯法解决子集问题
"""
n = 3
def find_subset():
    array = [1,1,2]
    temp = []
    res = []
    subset(array, 0, res, temp)
    print(res)
    
def isSafe(array, temp, res):
    if array not in temp:
        return True

def subset(array, pos, res, temp):
    inner_temp = sorted(temp).copy()
    if inner_temp not in res:
        res.append(inner_temp)
    if pos == n:
        return
    for i in range(n):
        if isSafe(array[i], temp, res):
            temp.append(array[i])
            subset(array, pos+1, res, temp)
            temp.pop()
if __name__ == "__main__":

    find_subset()