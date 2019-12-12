# encoding:utf-8

class DisjointSet(object):
    """
    并查集
    """
    def __init__(self):
        self.parent = []
    def find(self, i):
        # 找到i结点最上级的父节点
        if i == self.parent[i]:
            # 如果i就是父节点，那么停止搜索
            return i
        # 否则向父结点搜索
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, u, v):
        # v的父节点是u
        self.parent[v] = u

# 并查集

if __name__ == "__main__":
    pass