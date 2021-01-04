# encoding:utf-8
"""
问题描述：
input一个groupSizes,这个list里面的第i个元素的值代表这个元素在的groupSize的大小
比如[2,1,3,3,3,2]中2表示index=0的人所在的组别是大小为2的组
解决方法：
1）将groupSizes从小到大排序得到sorted_group，对应的index也重新排序得到sorted_index
2）将相同的元素分为一组，记录分割的split
3）将相同元素组里多于组大小的元素重新分为子组
[2,1,3,3,3,2] -> [1,2,2,3,3,3]
res_split = [0, 1, 3, 6]
[3,3,3,3,3,1,3]->[1,3,3,3,3,3,3]
res_split = [0, 1, 7]
[3,3,3,3,3,3]重新分子组[3,3,3], [3,3,3]

"""

class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        res = []
        sorted_index = [i[0] for i in sorted(enumerate(groupSizes), key=lambda x:x[1])]
        sorted_group = sorted(groupSizes)
        res_split = []
        for i,group_size in enumerate(sorted_group):
            if i+1<len(sorted_group):
                if group_size != sorted_group[i+1]:
                    res_split.append(i+1)
                else:
                    continue
        res_split.insert(0,0)
        res_split.append(len(sorted_index))
        print(res_split)
        for i in range(1, len(res_split)):
            split_sorted_group = sorted_group[res_split[i-1]:res_split[i]]
            split_sorted_group_mean = sum(split_sorted_group)/len(split_sorted_group)
            if split_sorted_group_mean<len(split_sorted_group):
                for j in range(res_split[i-1], res_split[i], split_sorted_group_mean):
                    res.append(sorted_index[j:j+split_sorted_group_mean])
            else:
                res.append(sorted_index[res_split[i-1]:res_split[i]])
        return res
            
if __name__ == "__main__":
    s = Solution()
    groupSizes = [3,3,3,3,3,1,3]
    
    print(s.groupThePeople(groupSizes))
