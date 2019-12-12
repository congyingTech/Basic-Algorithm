# encoding:utf-8
"""
问题描述：有向（可能有环图）图
"""
class DirectedGraph(object):
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = [[0]*self.vertices for i in range(self.vertices)]

    def add_edges(self, src, dest):
        self.graph[src][dest] = 1

    def print_graph(self):
        for i in range(self.vertices):
            connect_vertices = []
            for j in range(self.vertices):
                if self.graph[i][j] == 1:
                    connect_vertices.append(j)
            print('head:{}, connect with {}'.format(i, connect_vertices))
    # 深度搜索(backtrack)find path
    def print_path(self, i, temp, res):
        """
        i是第i个点
        """
        if len(set(temp))<len(temp):
            print('闭环:{}'.format(temp))
            inner_res = temp[:]
            res.append(inner_res)
            return 
        if 1 not in self.graph[i] and temp not in res :
            print(temp)
            inner_res = temp[:]
            res.append(inner_res)
            return
        
        for j in range(self.vertices):
            if self.graph[i][j] == 1:
                temp.append(j)
                self.print_path(j, temp, res)
                temp.pop()                

if __name__ == "__main__":
    v_num = 4
    graph = DirectedGraph(v_num)
    graph.add_edges(0,1)
    graph.add_edges(0,2)
    graph.add_edges(1,3)
    graph.add_edges(2,3)
    graph.add_edges(2,0)
    graph.print_graph()
    temp = [0] 
    res = []
    graph.print_path(0, temp, res)
    print(res)
    