#encoding:utf-8
n=3


def subsets(nums):
    res = []
    backtrack(res, [], nums, 0)
    return res

def backtrack(res, temp, nums, index):
    if list(set(temp)) not in res:
        res.append(list(set(temp[:])))
    if index==n:
        return
    for i in range(n):
        temp.append(nums[i])
        backtrack(res, temp, nums, index + 1)
        temp.pop() # Backtrack

if __name__ == "__main__":
     res = subsets('BCA')
     print(res)