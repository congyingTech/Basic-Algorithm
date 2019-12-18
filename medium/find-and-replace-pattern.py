# encoding:utf-8
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        def find_pattern_way(pattern):
            exists_word = [None]*len(pattern)
            pattern_way = [0]*len(pattern)
            pattern_way1 = [0]*len(pattern)
            for index in range(len(pattern)):
                if pattern[index] not in exists_word:
                    pattern_way[index] = 1
                    exists_word[index] = pattern[index]
                else:
                    exist_indices = [i for i, x in enumerate(exists_word) if x == pattern[index]]
                    exist_need_change_index = exist_indices[-1]
                    pattern_way[index] = pattern_way[exist_need_change_index] + 1
                    exists_word[index] = pattern[index]

                    for exist_indice in exist_indices:
                        pattern_way1[exist_indice]+=1
                    pattern_way1[exist_indice]+=1
                    pattern_way1[index] = pattern_way1[exist_indices[-1]]

            return pattern_way, pattern_way1
        pattern_way, pattern_way1 = find_pattern_way(pattern)
        for word in words:
            word_pattern_way, word_pattern_way1 = find_pattern_way(word)
            if word_pattern_way == pattern_way and word_pattern_way1 == pattern_way1:
                res.append(word)
        return res


if __name__ == "__main__":
    s = Solution()
    words = ["abc","deq","mee","aqq","dkd","ccc"]
    pattern = "abb"
    print(s.findAndReplacePattern(words, pattern))