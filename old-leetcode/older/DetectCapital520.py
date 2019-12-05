class Solution(object):
    def detectCapitalUse(self, word):
        upper_word = word.upper()
        word_ascii = sum([ord(e) for e in list(word)])
        upper_word_ascii = sum([ord(e) for e in list(upper_word)])
        subval = word_ascii-upper_word_ascii
        if subval == 0:
            return True
        if subval == len(word)*32:
            return True
        if subval == (len(word)-1)*32 and word[0].isupper():
            return True
        else:
            return False
        
        return word_ascii-upper_word_ascii

if __name__ == "__main__":
    word = ''
    print(Solution().detectCapitalUse(word))
