# encoding:utf-8
import sys
class DisjointSet(object):
    """
    并查集
    """
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
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

def maxdeadline(arr, n):
    max_d = -sys.maxsize-1
    for i in range(n):
        if arr[i]['deadline']>max_d:
            max_d = arr[i]['deadline']
    return max_d

def printjobscheduling(arr, n): 
    max_d = maxdeadline(arr, n)
    sorted_arr = sorted(arr, key=lambda x: x['profit'], reverse=True)
    ds = DisjointSet(max_d)
    for i in range(n):
        available_slot = ds.find(sorted_arr[i]['deadline'])
        if available_slot > 0:
            # 下一步的union的操作相当于把available_slot之前的设置为available的
            ds.union(ds.find(available_slot-1), available_slot)
            print(sorted_arr[i]['id']) 

# 并查集
if __name__ == "__main__":
    arr = [{'id': 'a', 'deadline': 2, 'profit': 100}, 
           {'id': 'b', 'deadline': 1, 'profit': 19}, 
           {'id': 'c', 'deadline': 2, 'profit': 27}, 
           {'id': 'd', 'deadline': 1, 'profit': 25}, 
           {'id': 'e', 'deadline': 3, 'profit': 15}] 
    n = len(arr)
    printjobscheduling(arr, n)