#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-07-17 00:07

双链表存储LRU的位置，哈希表存key-node，方便在O(1)时间找到node，然后进行操作
"""


class DLinkedNode(object):
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = dict()
        # tail和head是两个虚节点
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node = self.cache.get(key)
        val = node.value
        # key作为最近使用过的元素需要移动至双链表头部
        self.moveToHead(node)
        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache.get(key)
            node.value = value
            # 因为最近更新了值，所以移动到头部
            self.moveToHead(node)
        else:
            node = DLinkedNode(key, value)
            self.cache[key] = value
            if self.size == self.capacity:
                # 当size满的时候，去掉尾部的最后一个元素
                tail_node = self.removeTail()
                self.cache.pop(tail_node.key)
            else:
                self.size += 1
            self.addNodeToHead(node)

    def removeNode(self, node):

        next_node = node.next
        pre_node = node.prev
        pre_node.next = next_node
        next_node.prev = pre_node

    def addNodeToHead(self, node):
        head_next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next_node
        head_next_node.prev = node

    def moveToHead(self, node):
        self.removeNode(node)
        self.addNodeToHead(node)

    def removeTail(self):
        # tail_pre_node是要删除的节点
        tail_pre_node = self.tail.prev
        self.removeNode(tail_pre_node)
        return tail_pre_node


if __name__ == "__main__":
    capacity = 10
    s = LRUCache(capacity)
