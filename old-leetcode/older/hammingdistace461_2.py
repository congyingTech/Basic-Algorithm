
#-*-coding:utf-8-*-
import math
class Solution(object):
    result_x = [0]*31   
    result_y = [0]*31
    highest_x = 0
    highest_y = 0
    result = 0
    def hamming(self, x, y):
        if x > 0:
            self.highest_x = math.floor(math.log(x, 2))
            self.result_x[int(31-self.highest_x-1)] = 1
            temp_x = x - 2**self.highest_x
        else:
            temp_x = 0
        if y > 0:
            self.highest_y = math.floor(math.log(y, 2))
            self.result_y[int(31-self.highest_y-1)] = 1
            temp_y = y - 2**self.highest_y 
        else:
            temp_y = 0
        
        if temp_x == 0 and temp_y == 0:
            for i in range(31):
                if self.result_x[i] != self.result_y[i]:
                    self.result += 1
            return self.result
        
        self.hamming(temp_x, temp_y)
        
    def hammingDistance(self, x, y):
        self.hamming(x, y)
        return self.result
        
        
if __name__ == "__main__":
    x = 3;y = 1
    s = Solution()
    print(s.hammingDistance(x, y))
   
