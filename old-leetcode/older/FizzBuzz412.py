class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        n_l = list()
        for i in range(1,n+1):
            
            if i % 3 == 0 and i % 5 !=0:
                n_l.append('Fizz')
            elif i % 5 == 0 and i % 3 !=0:
                n_l.append('Buzz')
            elif i % 3 == 0 and i % 5 == 0:
                n_l.append('FizzBuzz')
            else:
                n_l.append(str(i))
        return n_l  
            
        
        
if __name__ == '__main__':
    n = 15
    print(Solution().fizzBuzz(n))
