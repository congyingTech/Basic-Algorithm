class Solution(object):
    def reverseWords(self, s):
        s_l = s.split(' ')
        #sorted 和 reversed 并不是可变对象的特有方法，可以接受字符串元组等不可变对象
        #而可变对象.sort()只针对可变对象，得到的结果是 可变对象本身发生了变化
        
        #这里的reversed可以用e[::-1]这样效率更高
        result = [''.join(reversed(e)) for e in s_l ] 
        return ' '.join(result)

if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    print(Solution().reverseWords(s))