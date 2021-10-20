# -*- coding: utf-8 -*-
# @Time    : 2021/10/20 10:44 上午
# @Author  : Mohn
# @FileName: 208-implement-trie-prefix-tree.py
"""
Trie树是一颗多叉树
children记录的是trie树的多个叉，isEnd是trie树insert word是否终止的标志

"""


class Trie(object):

    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self
        for ch in word:
            gap = ord(ch) - ord('a')
            if not node.children[gap]:
                node.children[gap] = Trie()
            node = node.children[gap]
        node.isEnd = True

    def searchPrefix(self, word):
        node = self
        for ch in word:
            gap = ord(ch) - ord('a')
            if not node.children[gap]:
                return None
            # 相当于指针中的next，指向下一个节点
            node = node.children[gap]
        return node

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # 当res存在且isEnd是True的情况下，这个完整的word才算是被找到
        res = self.searchPrefix(word)
        return res is not None and res.isEnd

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        res = self.searchPrefix(prefix)
        return res is not None


if __name__ == "__main__":
    trie = Trie()
