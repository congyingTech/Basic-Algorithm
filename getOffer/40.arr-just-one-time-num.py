#encoding:utf-8
"""
问题描述：
整型数组中，除了两个数字以外，其他的数字都出现了两次，找出那两个数字，要求时间复杂度是O(n),空间复杂度是O(1).
解决方案：
思路1）遍历求sum，然后去重求sum，然后去重后的sum*2 - originsum = x+y
那么这个问题就转化成target为固定值时，x，y分别是谁的问题：
对于 two sum的问题：
可以用target - list作为互补,生成互补的dict，后遍历list，如果list中的元素在互补数组中出现，那么这个元素就是要找的x和y。
这样做的空间复杂度是O(N)，不满足题目要求

思路2）用异或的方式：相同的数字异或的结果一定是0，所以arr进行异或的结果一定不为1，而是不同的两个数字x,y的异或。
那么如何将这x,y拆分出来呢，找到异或结果的某一位为1的位置，比如x^y结果是0011，那么位置可以是最左边位置的1，遍历所有的数，
将该位上为1的分为1组，该位为0的分为一组，为什么可以这么分呢？
因为异或是相异为1，如果x^y异或的结果在某一位置上为1，那么说明x，y在这一位不同，所以可以拆出来x，y
"""
class Solution(object):
    """
    该解法的空间时间复杂度都是O(n)，不满足题目要求
    """
    def findNum(self, arr):
        sum1 = sum(arr)
        sum2 = sum(set(arr))
        target = sum2*2-sum1
        res = self.twoSum(arr, target)
        print(res)

        
    def twoSum(self, nums, target):
        """
        时间复杂度是O(n)，空间复杂度是O(n)
        """
        pairSet = {}
        for i in range(0, len(nums)):
            if str(nums[i]) in pairSet:
                return [pairSet[str(nums[i])], i]
            pairSet[str(target - nums[i])] = i
        return [-1, -1]

class Solution1(object):
    def findNum(self, array):
        temp = array[0]
        for i in range(1, len(array)):
            temp = array[i]^temp
        print(temp)
        index = 1
        # index从0001开始找, &表示所有位置相同且都为1的话返回1，其他情况返回0
        # 如果temp&0001 == 0表示，temp的最后一位不是1，那么看index左移动即0010，如果temp&0010!=0,说明temp第二位和0010相同是1了
        # 从而找到temp第一个是1的位置
        while temp&index == 0:
            index=index<<1
        res1, res2 = 0, 0
        for num in array:
            if num&index == 0:
                res1 ^= num
            else:
                res2 ^= num

        print(res1, res2)
            

if __name__ == "__main__":
    s = Solution()
    arr = [9,2,3,3,4,4,5,5]
    #s.findNum(arr)
    #print(s.twoSum([3,3], 6))
    s1 = Solution1()
    s1.findNum(arr)