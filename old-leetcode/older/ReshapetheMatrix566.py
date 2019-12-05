
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(nums)
        n = len(nums[0])
        acc = m * n
        if r*c != acc:
            return nums
        numsl = [x for e in nums for x in e]
        #这种方式是浅拷贝，会导致后面赋值的时候同时改变同一列的值的，导致无法达到我们预期的效果
        # new_nums = [[0]*c]*r
        new_nums = [([0]*c) for i in range(r)]
        index = 0
        for i in range(r):
            for j in range(c):
                new_nums[i][j] = numsl[index]
                index+=1
        return new_nums

if __name__ == '__main__':
    nums = [[1,2],[3,4]]
    r = 4
    c = 1
    print(Solution().matrixReshape(nums, r, c))