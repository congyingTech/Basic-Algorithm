class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = list()
        for i,v in enumerate(nums):
            for j,u in enumerate(nums):
                if v + u == target and i not in result and j not in result and i != j:
                    result.append(i)
                    result.append(j)
        return result


class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buff_dict = {}
        for i,m in enumerate(nums):
            n = target-m
            if n in buff_dict:#n比的是字典里的k值
                return [buff_dict[n], i]
            else:
                buff_dict[m] = i

if __name__ == '__main__':
    s = Solution1()
    nums = [3,2,4]
    target = 6
    print(s.twoSum(nums, target))
    a = dict()
    a[1]=3
    a[2]=5

    print(2 in a)

