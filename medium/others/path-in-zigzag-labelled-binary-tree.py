# encoding:utf-8
# 问题描述：给定一颗满二叉树，这个二叉树的层序遍历是奇数层顺序排序，偶数层逆序排序
# exp: 4层满二叉树的层序遍历是：[1, 3,2, 4,5,6,7, 15,14,13,12,11,10,9,8]
# 解决方案：先根据label把二叉树的层数算出来，然后根据层数得到上述的层序遍历，分区寻找上一级的对应的元素

import math
class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        depth = int((math.log(label,2)))+1
        all_item = [i+1 for i in range(2**depth)]
        start_index= 1
        temp = []
        res_index = []
        for i in range(1, depth+1):
            if i % 2 != 0:
                part = all_item[start_index-1:2**i-1]
                temp.extend(part)
            else:
                part = all_item[start_index-1:2**i-1]
                temp.extend(part[::-1])
            start_index=2**i
        label_index = temp.index(label)
        
        while label_index>=0:
            res_index.append(label_index)
            if label_index%2==0:
                label_index = (label_index-2)/2
            else:
                label_index = (label_index-1)/2
        return [temp[i] for i in res_index][::-1]
                
if __name__ == "__main__":
    s = Solution()
    label = 14
    print(s.pathInZigZagTree(label))