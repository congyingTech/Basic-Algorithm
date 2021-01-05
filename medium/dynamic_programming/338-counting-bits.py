def count_num(num):
    """
    O(n*len(integer))的常规做法
    :param num:
    :return:
    """
    res = []
    for i in range(num+1):
        count = 0
        while i:
            if i & 1 == 1:
                count += 1
            i = i >> 1
            print(i)
        res.append(count)
    print(res)


if __name__ == "__main__":
    count_num(4)
