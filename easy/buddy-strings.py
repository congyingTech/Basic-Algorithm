#coding:utf-8

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        A_l = len(A)
        B_l = len(B)
        if A_l != B_l:
            return False
        if A==B=="":
            return False
        A = list(A)
        B = list(B)
        if A_l==2 and A[0]==B[1] and A[1]==B[0]:
            return True
        elif A_l==2:
            return False 
        
        diff_pos = []
        for i in range(A_l):
            if A[i]!=B[i]:
                diff_pos.append(i)
        if len(diff_pos) == 2 and A[diff_pos[0]]==B[diff_pos[1]] and A[diff_pos[1]==A[diff_pos[0]]]:
            return True
        elif len(diff_pos) == 0 and len(set(A))<A_l:
            return True
        else:
            return False 
        


        # if res and (count == 1 or count ==0) and len(set(A))<A_l:
        #     return True
        # else:
        #     return False
        
                
if __name__ == "__main__":
    s = Solution()
    A = "abab"
    B = "abab"
    res = s.buddyStrings(A,B)
    print(res)
