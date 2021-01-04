# encoding:utf-8
"""
ababcbacadefegdehijhklij
to
ababcbaca efegdeh ijhklij
问题描述：给出小写字母的字符串S。我们希望将此字符串分成尽可能多的部分，以便每个字母最多显示一个部分，并返回代表这些部分大小的整数列表。
解决思路：贪心的想法，step1:字符串S的每一个字符出现的最后位置进行标记存到last里面；step2:anchor和j分别是子label的起点和终点;
step3:遍历S，直到i和j相等，这说明，i之前的所有的字母的last index都比j小，包含在j之前。
"""
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = {c: i for i,c in enumerate(S)}
        anchor = 0
        j = 0
        ans = []
        for i,c in enumerate(S):
            j = max(j, last.get(c))
            if i == j:
                ans.append(j-anchor+1)
                anchor = i+1
        return ans


if __name__ == "__main__":
    s = Solution()
    S = 'ababcbacadefegdehijhklij'
    print(s.partitionLabels(S))
    
