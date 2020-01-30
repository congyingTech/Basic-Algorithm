# encoding:utf-8
"""
问题描述：根据后序遍历数组判断是不是bst树
解决方案：input = [0,2,1,5,4,3]
bst树左边总比根节点小，右边总比根节点大，所以0，2，1是左子树，5，4，3是右子树，再判断左右子树是不是bst树
"""

class Solution(object):
    def isBst(self, input_arr):
        root_val = input_arr[-1]
        n = len(input_arr)
        for i in range(n):
            if input_arr[i]>root_val:
                break
        left_vals = input_arr[:i]
        right_vals = input_arr[i:-1]   
        # 判断划分点右边的数组是否还有比根节点小的，如果有就是False
        for val in right_vals:
            if val<root_val:
                return False
        left= True
        if i>0:
            left = self.isBst(left_vals)
        right = True
        if i<n-1:
            right = self.isBst(right_vals)

        return left and right
    
        
        

if __name__ == "__main__":
    s = Solution()
    input_arr = [0,2,9,1,5,4,2,3]
    print(s.isBst(input_arr))