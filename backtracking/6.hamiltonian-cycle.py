#encoding:utf-8
class AdjNode(object):
    """
    邻接结点
    """
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * self.vertices
    
    def add_edges(self, src, dest):
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

def isSafe(index, temp, n):
    if index not in temp and index <= n:
        return True
    return False 


def hamiltonianCycleUtil(start_node_index, graph,n,temp):
    if len(temp) == n:
        return True
    possible_node_index = []
    node = graph[start_node_index]
    while node:
        possible_node_index.append(node.vertex)
        node = node.next
    for index in possible_node_index:
        if isSafe(index, temp, n) == True:
            temp.append(index)
            if hamiltonianCycleUtil(index, graph, n, temp)==True:
                return True
            temp.remove(index)

def hamiltonianCycleSolve(graph, n):
    start_node_index = 0
    temp = [start_node_index]
    if hamiltonianCycleUtil(start_node_index, graph,n,temp) == True:
        start_node = graph[temp[0]]
        end_node = graph[temp[-1]]
        res1 = False
        res2 = False
        # 判断是否首位相连接，如果连接的话，就是hamiltonian环
        while start_node:
            if start_node.vertex == temp[-1]:
                res1 = True
                break
            start_node = start_node.next
        while end_node:
            if end_node.vertex == temp[0]:
                res2 = True
                break
            end_node = end_node.next
        res = res1&res2
        if res == True:
            print('Hamiltonian exists and show as {}'.format(temp))
        else:
            print('This is an diag has closed loop, but hamiltonian cycle doesnt exists. and temp path is {}'.format(temp))
    else:
        print("code has bug...")
    
if __name__ == '__main__':
    n = 5
    graph = Graph(n)
    graph.add_edges(0,1)
    graph.add_edges(0,3)
    graph.add_edges(1,2)
    graph.add_edges(1,3)
    graph.add_edges(1,4)
    graph.add_edges(2,4)
    graph.add_edges(4,3)
    # graph.add_edges(0,1)
    # #graph.add_edges(1,2)
    # #graph.add_edges(0,2)
    # graph.add_edges(2,3)

    hamiltonianCycleSolve(graph.graph, n)
    
