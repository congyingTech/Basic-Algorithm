str = input("请输入n：");
print ("你输入的内容是: ", int(str))
print(type(int(str)))

# 递归的参数是result 和 n


def digui(result, str):
    n = int(str)
    if n==1:
        return result.append(n)
    result.append('1')
    for item in result:
        for i in range(n+1):

            result.append((list(item).insert(i, n)).join(''))

    return result


if __name__ == '__main__':
    result = list()
    content = input("请输入n：");
    print("你输入的内容是: ", int(content))

    digui(result, str)
    print(result)
