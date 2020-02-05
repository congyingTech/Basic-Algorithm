# encoding:utf-8
"""
问题描述：
题目1:翻转单词顺序。I am a student.  --->  student. a am I
题目2:左旋转字符串。  向左翻转2个字母变成 cdefgab

解决方案：
1）思路：先reverse整个sentence，然后把每个sentence中的每个单词单独reverse。
2）思路：可以用和1）很相似的解法。
"""

class Solution(object):
    def reverseWord(self, sentence):
        reversedSentence = self.reverse(sentence, 0, len(sentence)-1)
        reversed_words = reversedSentence.split(' ')
        res = ''
        for word in reversed_words:
            new_word = self.reverse(word, 0, len(word)-1) + ' '
            res += new_word
        print(res)
    
    def reverse(self, sentence, start, end):
        sentence = list(sentence)
        if start==0 and end==0:
            return ''.join(sentence)
        while start<=end:
            temp = sentence[start]
            sentence[start] = sentence[end]
            sentence[end] = temp
            start += 1
            end -= 1
        return ''.join(sentence)

class Solution1(object):
    def leftTransStr(self, string, k):
        left_part = string[:k]
        right_part = string[k:]
        return right_part + left_part

if __name__ == "__main__":
    s = Solution()
    sentence = 'I am a student.'
    s.reverseWord(sentence)
    string = 'abcdefg'
    s1 = Solution1()
    print(s1.leftTransStr(string, 2))