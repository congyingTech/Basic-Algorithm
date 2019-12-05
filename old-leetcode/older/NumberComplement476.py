import math
class Solution(object):
    
    def findComplement(self, num):
        lenth = len(bin(num))-2
        one_num = 2**lenth-1
        #与全1的数字进行异或，得到按位取反的数值
        rev_num = num^one_num
        
        return rev_num
        
       
        
if __name__ == "__main__":
    print(Solution().findComplement(1))
