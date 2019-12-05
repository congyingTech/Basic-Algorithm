class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote_set = list(set(ransomNote))
        flag = 0
        for i in ransomNote_set:
            if i in magazine:
                if ransomNote.count(i) <= magazine.count(i):
                    flag += 1
            else:
                return False
        if flag == len(ransomNote_set):
            return True
        else:
            return False
                
if __name__ == '__main__':
    s = Solution()
    ransomNote,magazine = "abcc", "banana count coook"
    print(s.canConstruct(ransomNote, magazine))
