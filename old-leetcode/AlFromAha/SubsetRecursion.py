def subset(index):
    """
    求子集的递归方法
    :return:
    """
    n = len(array)
    subSet=list()
    if index == n:
       print(allSet)
       return
    else:
        for i in allSet:
            ele = list()
            ele.append(array[index])
            ele.extend(i)
            subSet.append(ele)
    allSet.extend(subSet)
    subset(index + 1)




if __name__ =="__main__":
    array = [1,2,3,4,5,6]
    index = 0
    allSet = list()
    allSet.append([])
    subset(index)