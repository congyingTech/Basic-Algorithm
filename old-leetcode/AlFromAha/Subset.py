def subset():
    """求子集
    Args：subset--存放遍历的i元素时，它与已经生成的所有集合进行合并，产生新的集合
          allSet--存放所有的集合，集合也是list的形式
          ele--存放i元素和遍历allSet时，i与allSet中的每个子集extend形成的新的list
    AlSteps：
          1.allSet=[[]] #这一步非常重要，先加入空集
             2.开始遍历array，subset创建，存放因为i的加入产生的所有子集，下一步就是试图得到新产生的集合
                 3.遍历allSet，创建ele，存放allSet中的元素与i合并产生的新元素，每次循环ele只有一个元素
                 4.将新的ele元素加入subset中
             5.将由于i加入而产生的集合subset拓展到allSet中，用extend的原因是，subset的list中存放的也是list元素，所以我们要把subset中
               的list元素拓展到allSet中，当作allSet中的一个元素，而不是将[[]]放入到allSet中。
          6.打印结果

    Tips：
          python中的extend == Java中的addAll，都是将集合中的元素追加
    :return:
    """
    allSet = list()#存放所有子集的动态list
    allSet.append([])#初始化进去一个空集
    for i in array:
        subset=list() #存放当遍历到某个数的时候，它与allSet合并所产生的所有子集集合
        for j in allSet:
            ele=list() #存放此次j循环产生的新元素
            ele.append(i) #首先将i加入
            ele.extend(j) #其次将j中的list元素追加到i的后面
            subset.append(ele) #将遍历到的元素加入subset
        allSet.extend(subset) #将subset中的元素追加到allSet中
    print(allSet)

if __name__ == "__main__":
    array = [1,2,3,4,5,6]#待求子集的数组
    subset()
