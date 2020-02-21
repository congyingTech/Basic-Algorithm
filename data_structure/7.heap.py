# encoding:utf-8
""" 
reference：https://www.cnblogs.com/wangchaowei/p/8288216.html

堆结构：1）完全二叉树 2）heap中存储的值是偏序的
    1）最小堆：父节点的值比其他元素都要小 
    2）最大堆：父节点的值比其他元素都要大

堆的存储：一般用数组存储堆，i的左右子节点位置分别是2*i+1, 2*i+2，父节点的坐标是(i-1)/2

堆的操作：insert —— 简而言之是插入位置的父节点至根节点的序列的插入排序
    插入一个元素：新元素被加入到heap的末尾，然后更新树以恢复堆的次序。
    每次插入都是将新数据放在数组最后。
    可以发现从这个新数据的父结点到根结点必然为一个有序的数列，现在的任务是将这个新数据插入到这个有序数据中——这就类似于直接插入排序中将一个数据并入到有序区间中。
堆的操作：deleteMax
    按定义，堆中每次都删除第0个数据。
    为了便于重建堆，实际的操作是将最后一个数据的值赋给根结点，然后再从根结点开始进行一次从上向下的调整。
    调整时先在左右儿子结点中找最大的，如果父结点比这个最小的子结点还大说明不需要调整了，反之将父结点和它交换后再考虑后面的结点。
    相当于从根结点将一个数据的“下沉”过程。
建立堆数组：buildHeap
    [1,2,3,4,5,6,7] 不用从n开始调整，只用从n/2-1调整之前的位置的节点

堆排序：
    就是取数组的第一个元素，然后每次执行deleteMax的操作调整堆
"""


class heap(object):
    """
    大根堆
    """
    def __init__(self, heap):
        self.heap = heap
    
    def buildHeap(self):
        """
        建堆数组
        """
        if len(self.heap)<2:
            return self.heap
        if len(self.heap) == 2:
            if self.heap[0] < self.heap[1]:
                temp = self.heap[0]
                self.heap[0] = self.heap[1]
                self.heap[1] = temp
            return self.heap
        start_index=int(len(self.heap)/2)-1
        while start_index>=0:
            self.heap = self.siftdown(start_index, len(self.heap), self.heap)
            start_index -= 1
        return self.heap

    def insert(self, val):
        """
        堆中插入元素，是插入到数组尾部，插入的时候相当于对插入节点父节点的插入排序
        """
        n = len(self.heap)
        self.heap.append(val)
        while n>0:
            last_index = int((n-1)/2)
            if self.heap[n]>self.heap[last_index]:
                temp = self.heap[last_index]
                self.heap[last_index] = self.heap[n] 
                self.heap[n] = temp
            n = last_index
        return self.heap
             
    def deleteMax(self):
        """
        删除最大的元素
        """
        # 第一个元素是要被输出的元素，将第一个元素输出，将最后一个元素填充上第一个元素
        maxHeap = self.heap[0]
        self.heap[0] = self.heap[-1]
        arr.remove(self.heap[-1])
        self.heap = self.buildHeap()

        return maxHeap, self.heap

    def siftdown(self, i, n, arr):
        """
        自上而下的调整，将根节点下沉的过程
        i是调整的位置
        """
        while 2*i+2 < n:
            left_child = arr[2*i+1]
            right_child = arr[2*i+2]
            if left_child > right_child:
                change_index = 2*i+1
                max_child = left_child
            else:
                change_index = 2*i+2
                max_child = right_child

            if max_child>arr[i]:
                temp = arr[i]
                arr[i] = max_child
                arr[change_index] = temp
                if change_index<n:
                    i = change_index
            else:
                break
        return arr
                
    def heapsort(self):
        sorted_res = []
        while self.heap:
            maxHeap, self.heap = self.deleteMax()
            sorted_res.append(maxHeap)
        return sorted_res

if __name__ == "__main__":
    arr = [1,3,5,7, 9]
    heap1 = heap(arr)
    built_heap_arr = heap1.buildHeap()
    print('数组建堆：', built_heap_arr)
    built_heap = heap(built_heap_arr)
    after_insert_heap_arr = built_heap.insert(9)
    print('插入元素后的最大堆：', after_insert_heap_arr)
    after_insert_heap = heap(after_insert_heap_arr)
    sorted_heap_res = after_insert_heap.heapsort()
    print('对上述的堆排序：', sorted_heap_res)


