# encoding:utf-8

### 图有两种表达方式，一种是邻接矩阵，一种是邻接表，在稀疏图情况下，邻接矩阵浪费了大量的空间，所以有了邻接表的出现

class AdjNode(object):
    """
    邻接结点
    """
    def __init__(self, data):
        self.vertex = data
        self.next = None
        

class Graph(object):
    """
    无向无权值图邻接表表示法
    """

    def __init__ (self, vertices):
        self.vertices = vertices
        self.graph = [None] * self.vertices
    
    def add_edges(self, src, dest):
        """
        无向图的两个结点相互指向，所以邻接表互相添加
        """
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(self.vertices):
            print("Adjacency list of vertex {}\n head".format(i)) 
            temp = self.graph[i] 
            while temp: 
                print(" -> {}".format(temp.vertex)) 
                temp = temp.next
            print('\n')

class Graph1(object):
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0]*self.vertices for j in range(self.vertices)]
    
    def add_edges(self, src, dest):
        self.graph[src][dest] = 1
        self.graph[dest][src] = 1

    def print_graph(self):
        for i in range(self.vertices):
            connect_vertices = []
            for j in range(self.vertices):
                if self.graph[i][j] == 1:
                    connect_vertices.append(j)
            print('head:{}, connect with {}'.format(i, connect_vertices))





if __name__ == "__main__":
    vertices = 5
    graph = Graph(5)
    graph.add_edges(0,1)
    graph.add_edges(1,2)
    graph.add_edges(0,2)
    graph.add_edges(2,3)
    graph.add_edges(2,4)
    graph.print_graph()

    graph1 = Graph1(5)
    graph1.add_edges(0,1)
    graph1.add_edges(1,2)
    graph1.add_edges(0,2)
    graph1.add_edges(2,3)
    graph1.add_edges(2,4)
    graph1.print_graph()
