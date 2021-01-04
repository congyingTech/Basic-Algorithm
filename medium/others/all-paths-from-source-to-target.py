#encoding:utf-8
"""
问题描述：给定N个nodes的有向无环图，求所有的通路
解决方案：例如
Input: [[1,2], [3], [3], []] 
0--->1
|    |
\/   \/
2--->3

Output: [[0,1,3],[0,2,3]]
就是有向图的路径输出，可以用backtrack的思路
"""
class DirectedGraph(object):
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = [[0]*self.vertices for i in range(self.vertices)]

    def add_edges(self, src, dest):
        self.graph[src][dest] = 1

class Solution(object):
    def print_path(self, i, temp, res, n, directed_graph):
        """
        i是第i个点
        """
        if 1 not in directed_graph[i] and temp not in res :
            inner_res = temp[:]
            res.append(inner_res)
            return
        
        for j in range(n):
            if directed_graph[i][j] == 1:
                temp.append(j)
                self.print_path(j, temp, res, n, directed_graph)
                temp.pop()

    def allPathsSourceTarget(self, graph):
        """
        :type graph: [[1,2], [3], [3], []] 
        :rtype:  [[0,1,3],[0,2,3]]
        """
        directed_graph = DirectedGraph(len(graph))
        for i, items in enumerate(graph):
            if items:
                for item in items:
                    directed_graph.add_edges(i,item)
        temp = [0] 
        res = []
        n = len(graph)
        self.print_path(0, temp, res, n, directed_graph.graph)
        print(res)
            
        
if __name__ == "__main__":
    s = Solution()
    
    graph = [[1,2], [3], [3], []] 
    s.allPathsSourceTarget(graph)

