# encoding:utf-8
"""
m着色问题
m是可以选择着色的颜色数
v_num是点的个数
"""
class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0]*self.vertices for j in range(self.vertices)]
    
    def add_edges(self, src, dest):
        self.graph[src][dest] = 1
        self.graph[dest][src] = 1


def isSafe(v, v_num, graph, c, color):
    """
    v是第v个点，v_num是点的个数，graph是图，c即将着色的颜色，color是当前行涂的色
    """
    for i in range(v_num):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True
    

def solveColorUtil(v, m, v_num, graph,color):
    """
    m是可以选择着色的颜色数
    """
    if v == v_num:
        return True
   
    for c in range(m):
        if isSafe(v, v_num, graph, c, color) == True:
            color[v] = c
            if solveColorUtil(v+1,m,v_num,graph,color)==True:
                return True
            color[v] = 0

def solveColor(m, v_num, graph):
    v=0
    color = [-1]* v_num
    if solveColorUtil(v,m,v_num,graph,color)==None:
       print('Code has bug!')
       return 
    print('{} color exists: {}'.format(m, color))

if __name__ == "__main__":
    m = 3
    v_num = 4
    graph = Graph(v_num)
    graph.add_edges(0,1)
    graph.add_edges(0,2)
    graph.add_edges(0,3)
    graph.add_edges(1,2)
    graph.add_edges(2,3)

    solveColor(m, v_num, graph.graph)
