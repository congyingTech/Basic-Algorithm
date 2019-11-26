class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        trans_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        words_list = []
        for word in words:
            word_res = []
            for c in word:
                c_val = ord(c)
                c_map = trans_list[c_val-97]
                word_res.append(c_map)  
            words_list.append(''.join(word_res))
        return len(set(words_list))

if __name__ == "__main__":
    s = Solution()
    words = ["gin", "zen", "gig", "msg"]
    res = s.uniqueMorseRepresentations(words)
    print(res)