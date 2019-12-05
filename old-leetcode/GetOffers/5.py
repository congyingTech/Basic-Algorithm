# 两个栈实现一个队列, pythond的list可以当作一个栈
# -*- coding:utf-8 -*-
class Queue:
    def __init__(self, list=[]):
        self.list = list
    def push(self, node):
        self.list.append(node)

    def pop(self):
        temp = [self.list[i] for i in range(len(self.list)-1,-1, -1)]
        print(temp[0])
        self.list.pop()

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if len(self.stack2) != 0:  # 如果stack2中还有残留的，应该先把残留的给pop出来，再进行下一步
            return self.stack2.pop()
        elif len(self.stack1)==0:
            return None
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


if __name__ == "__main__":
    # s = Queue()
    # s.push(1)
    # s.pop()
    # s.push(2)
    # s.pop()
    #"PSH1", "PSH2", "PSH3", "POP", "POP", "PSH4", "POP", "PSH5", "POP", "POP"]
    s = Solution()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    s.pop()
    s.push(4)
    s.pop()
    s.push(5)
    s.pop()
    s.pop()

