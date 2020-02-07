# encoding:utf-8
"""
问题描述：
请实现一个函数，用来匹配包含‘.’和‘*’的正则表达式。
.表示任意一个字符；*表示前一个字符可以出现任意次(包括0次)
解决方案：
）比较工程的问题，可以分别对string和pattern设定一个p1，p2，然后循环
"""


class Solution(object):
    def regularMatch(self, string, pattern):
        p1=0
        p2=0
        while p1<len(string) and p2<len(pattern):
            while p1<len(string) and p2<len(pattern) and string[p1] != pattern[p2]:
                if pattern[p2] == '.':
                    p1+=1
                    p2+=1
                elif pattern[p2+1] == '*':
                    p2+=2
                    if pattern[p2] != string[p1]:
                        return False
                    else:
                        p1+=1
                        p2+=1
                else:
                    return False
                
            else:
                p1+=1
                p2+=1
        return True    
                    

if __name__ == "__main__":
    s = Solution()
    string = 'aaa'
    pattern = 'bb*abx*a'
    print(s.regularMatch(string, pattern))