# coding=utf-8
"""
@author: congying
@email: wangcongyinga@gmail.com 
@time: 2019/1/31
"""

def default_quick_sort(data, left, right):
    """
    快速排序:每次找到一个基准，尾部先走，找到<pivot的数停下，头部再走，找到>pivot的数停下，如果i<j
    的话，两个位置的数交换，如此这般直到i==j,记录下当前的位置，把pivot和当前位置的数交换，然后分别对左右
    两边的子序列进行快排
    """
    if left > right:
        return
    pivot = data[left]
    i,j = left, right
    while i!=j:
        while i<j and data[j]>=pivot:
            j -= 1
        while i<j and data[i]<=pivot:
            i += 1
        if i<j:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
        
    data[left] = data[i]
    data[i] = pivot
    default_quick_sort(data,left, i-1)
    default_quick_sort(data, i+1, right)
    
    
        
def default_shell_sort(data):
    """
    希尔排序——希尔排序的基本思想是在插入排序的基础上把data分组，分组的规则一般是一定步长间隔，步长间隔初始化是length/2, 后来的步长是前一个步长/2
    然后把每个分组内的数据进行插入排序
    时间复杂度是O(n^3/2)，是不稳定的排序算法
    :param data:
    :return:
    """
    n = len(data)
    gap = n / 2  # 步长

    while gap >= 1:
        temp_data = []
        for i in range(gap):
            inner_data = []
            for j in range(i, n, gap):
                inner_data.append(data[j])
            temp_data.extend(default_insert_sort(inner_data))
        data = temp_data
        gap = gap / 2
    return data


def default_insert_sort(data):
    """
    插入排序——default插入排序的思想就是遍历一遍数据，把新遍历到的数据插入到已经排好序的list里面
    时间复杂度是O(n^2)，结合平衡二叉树的插入排序时间复杂度是O(n*logn)
    :param data:
    :return:
    """
    n = len(data)
    for i in range(n):
        for j in range(i, -1, -1):
            if j == 0:
                continue
            if data[j] < data[j - 1]:
                temp = data[j]
                data[j] = data[j - 1]
                data[j - 1] = temp
    return data


def default_bubble_sort(data):
    """
    冒泡排序——从小到大的冒泡排序的基本思想是小泡冒出，大泡沉底
    时间复杂度是O(n^2)
    :param data:
    :return:
    """
    n = len(data)
    for i in range(n):
        max_data = data[0]
        for j in range(1, n):
            if max_data > data[j]:
                temp = data[j]
                data[j] = max_data
                data[j - 1] = temp
            else:
                max_data = data[j]
    return data


def default_merge_sort(data):
    """
    归并排序——基本思想是分而治之，8 4 5 7 1 3 6 2, 治->4578, 1236  tmp=[1,2,3,4,5,6,7,8]
    :param data:
    :return:
    """
    n = len(data)
    if n <= 1:
        return
    mid = n / 2
    data_left = data[0: mid]
    data_right = data[mid: n]
    m = max(len(data_left), len(data_right))
    i = 0
    j = 0
    data_temp = []
    default_merge_sort(data_left)
    default_merge_sort(data_right)

    while m > 0:
        if data_left[i] > data_right[j]:
            data_temp.append(data_right[j])
            j += 1
        else:
            data_temp.append(data_left[i])
            i += 1
        m -= 1


def default_heap_sort(data):
    """
    堆排序——堆排序是选择排序的一种。
    1.堆的概念：堆是具有以下性质的完全二叉树：每个结点的值都大于或等于其左右孩子结点的值，称为大顶堆；或者每个结点的值都小于或等于其左右孩子结点的值，称为小顶堆。
    2.完全二叉树的基本位置：n是data的长度，i是当前节点下标，最后一个非叶子节点(n/2-1), 非叶子节点的左孩子(2*i+1)，右孩子(2*i+2)
    3.堆排序基本思想：将待排序序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的根节点。将其与末尾元素进行交换，此时末尾就为最大值。然后将剩余n-1个元素重新构造成一个堆，这样会得到n个元素的次小值。如此反复执行，便能得到一个有序序列了
    4.堆排序的步骤：1）先建堆，时间复杂度是O(n) 2）后自上而下的下沉调节 (ps:建堆的过程和下沉的过程很像，建堆是从最后一个非叶子节点开始调整，下沉是从根结点开始调整)
    5.时间复杂度为O(n*logn)
    :param data:
    :return:
    """

    #  1.建堆
    n = len(data)
    i = 1
    while n >= 2 * i:
        root_index = n / 2 - i
        adjust_heap(data, root_index)
        i += 1
    #  2.下沉


    # 错误的解法：
    # for i in range(n, 0, -1):  # 要排列n个数，所以倒序数n轮
    #     iter_data = data[:i]  # 每一轮最后的i个数一定是排好序的,所以只用对n-i个数进行对排序
    #     m = len(iter_data)  # 每一轮的data的长度是m
    #     j = 1
    #     while m >= 2 * j:
    #         root_index = m / 2 - j
    #         left_index = 2 * root_index + 1
    #         right_index = 2 * root_index + 2
    #         if left_index < m and iter_data[root_index] < iter_data[left_index]:
    #             iter_data = swap_data(iter_data, left_index, root_index)
    #         if right_index < m and iter_data[root_index] < iter_data[right_index]:
    #             iter_data = swap_data(iter_data, right_index, root_index)
    #         j += 1
    #     data[:i] = iter_data
    #     data = swap_data(data, 0, i - 1)
    return data


def adjust_heap(data, root_index):
    """
    堆辅助函数——适应性调整堆
    :param data:
    :param root_index:
    :return:
    """
    m = len(data)
    while 2 * root_index <= m:
        left_index = 2 * root_index + 1
        right_index = 2 * root_index + 2
        if left_index < m and right_index < m:
            if data[left_index] < data[right_index]:
                child_index = right_index
            else:
                child_index = left_index
        elif left_index > m:
            child_index = right_index
        else:
            child_index = left_index
        if data[child_index] > data[root_index]:
            swap_data(data, root_index, child_index)
            root_index = child_index
        else:
            break
    return data


def swap_data(data, i, j):
    """
    堆辅助函数——交换元素
    :param data:
    :param i:
    :param j:
    :return:
    """
    temp = data[i]
    data[i] = data[j]
    data[j] = temp
    return data


def binary_search(data, target):
    start = 0
    if len(data) <= 0:
        print False
        return
    end = len(data) - 1
    mid = (end - start + 1) / 2
    data_left = data[start: mid]
    data_right = data[mid + 1: end + 1]
    if target < data[mid]:
        binary_search(data_left, target)
    elif target > data[mid]:
        binary_search(data_right, target)
    else:
        print True


def random_data():
    import random
    data = []
    for i in range(10):
        a = random.randint(0, 10)
        data.append(a)
    return data


if __name__ == "__main__":
    # data = [8, 9, 1, 7, 2, 3, 5, 4, 6, 0]
    # data = range(10)
    # for i in range(10):
    #     binary_search(data, i)
    # binary_search(data, -13532532542)

    # 快速排序
    data = random_data()
    print 'befort sort->', data
    default_quick_sort(data, 0, len(data)-1)
    print 'after insert sort->', data

    # 插入排序
    data = random_data()
    print 'befort sort->', data
    print 'after insert sort->', default_insert_sort(data)

    # 冒泡排序
    data = random_data()
    print 'befort sort->', data
    print 'after burble sort->', default_bubble_sort(data)

    # 希尔排序
    data = random_data()
    print 'before sort->', data
    print 'after shell sort->', default_shell_sort(data)

    # 归并排序
    data = random_data()
    print 'before sort->', data
    # print 'after merge sort->', default_merge_sort(data)

    # 堆排序
    # data = random_data()
    data = [4, 6, 1, 8, 1, 0, 9, 2, 0, 4]
    print 'before sort->', data
    print 'after heap sort->', default_heap_sort(data)