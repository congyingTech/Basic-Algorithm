class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MASK = 0x100000000
        #max_int是long int的最大值
        MAX_INT = 0x7FFFFFFF
        def add(a,b):
            if b==0:
                return a
            #1.获得个位数的值
            num1 = (a^b) % MASK
            #2.获得进位值，按位与只有1&1时，才为1，然后左移一位，可以获得进位
            num2 = ((a&b)<<1) % MASK
            
            return self.getSum(num1, num2)
        res = add(a,b)
        
        if res <= MAX_INT:return res
        else:return res | (~MASK+1)
        
        
if __name__ == "__main__":
    s = Solution()
    print(s.getSum(-3,-6))