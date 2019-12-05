class Solution(object):
    
    #效率比较低，可以看看效率更高的算法
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        submax = 0
        lenth = len(findNums)
        res_l = list()
        for i in range(lenth):
            if findNums[i] in nums:
                in2 = nums.index(findNums[i])
            if in2 < len(nums)-1:
                sub_l = nums[(in2+1):]
                submax = max(sub_l)
                if findNums[i] >= submax:
                    res_l.append(-1)
                else:
                    for j in range(len(sub_l)):
                        if sub_l[j] > findNums[i]:
                            res_l.append(sub_l[j])
                            break
            else:
                res_l.append(-1)
                
            
        return res_l
                    
             
        


if __name__ == '__main__':
    nums1 = [2,1,3]
    nums2 = [2,3,1]
    print(Solution().nextGreaterElement(nums1, nums2))