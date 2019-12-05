class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set = list(set(nums1))
        nums2_set = list(set(nums2))
        res = []
        for e in nums1_set:
            if e in nums2_set:
                res.append(e)
        return res
        
if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 2,4,3, 1]
    nums2 = [2, 2,3]
    print('helloworld')
    print(s.intersection(nums1, nums2))