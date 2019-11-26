# encoding:utf-8
n=3
"""
用回溯法解决全排列问题
"""

def printSolution(res):
    for i in res:
        print(i)

def isSafe(pos, i, ind_record):
    if ind_record[i]==False and pos < n:
        return True
    
def solvePermutation():
    array = 'CAC'
    res = []
    pos = 0
    temp = []
    ind_record = [False, False, False]
    solvePermutationUtil(res, array, pos, temp, ind_record)
    if res:
        printSolution(res)
    else:
        print('Fail!')


def solvePermutationUtil(res, array, pos, temp, ind_record):
    if pos == n and temp not in res:
        res.append(temp[:])
        return
    for i in range(n):
        if isSafe(pos, i, ind_record):
            temp.append(array[i])
            ind_record[i] = True
            solvePermutationUtil(res, array, pos+1, temp, ind_record)
            ind_record[i] = False
            temp.pop()

if __name__ == '__main__':
    solvePermutation()
