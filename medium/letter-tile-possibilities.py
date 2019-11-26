# encoding:utf-8
"""
全排列的问题
"""

class Solution(object):
    """
    没有pass的版本
    """
    def isSafe(self, visit_record_i, pos, n):
        if visit_record_i==False and pos<n:
            return True

    def backtiles(self, array, temp, res, pos, visit_record, n):
        if temp not in res:
            inner = temp.copy()
            res.append(inner)
        if pos == n:
            return 
        for i in range(n):
            if self.isSafe(visit_record[i], pos, n):
                temp.append(array[i])
                visit_record[i] = True
                self.backtiles(array, temp, res, pos+1, visit_record, n)
                visit_record[i] = False
                temp.pop()

    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        temp = []
        res = []
        array = list(tiles)
        n = len(array)
        visit_record = [False]*n
        self.backtiles(array, temp, res, 0, visit_record, n)
        return res

class Solution1(object):
    """
    pass的版本
    把res从list改为set，可以把时间从O(n)节省为O(1)
    """

    def isSafe(self, visit_record_i, pos, n):
        if visit_record_i==False and pos<n:
            return True

    def backtiles(self, array, temp, res, pos, visit_record, n):
        if temp not in res and temp:
            #inner = temp.copy()
            res.add(temp)
        if pos == n:
            return
        for i in range(n):
            if self.isSafe(visit_record[i], pos, n):
                temp += array[i]
                visit_record[i] = True
                self.backtiles(array, temp, res, pos+1, visit_record, n)
                visit_record[i] = False
                temp = temp[:-1]

    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        temp = ''
        res = set()
        #array = list(tiles)
        n = len(tiles)
        visit_record = [False]*n
        self.backtiles(tiles, temp, res, 0, visit_record, n)
        return len(res)



    




if __name__ == "__main__":
    s = Solution()
    res = s.numTilePossibilities('AAB')
    print(res)


