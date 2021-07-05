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


def count_num1(num):
    """
    建表法：O(n*1)，空间复杂度O(256)
    规律：
    奇数：奇数的1（0001）的个数是1个，奇数3（0101）的个数是2个，奇数5的个数是（1001）的个数是2个，相当于5/2=2的位数+1
    n的二进制中1的个数是n/2中1的个数+1，5相当于2右移一位（2*2=4）+1
    偶数：偶数2(0010)的个数1，偶数4(1000)的个数1，偶数6(1010)的个数是2个，相当于3右移动一位，所以6中1的个数等于3中1的个数
    :return:
    """
    pass



if __name__ == "__main__":
    count_num(4)
