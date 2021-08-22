#!/usr/bin/env python
# encoding: utf-8
"""
@author:Mohn
@email:wangcongyinga@gmail.com
@time: 2021-08-09 23:16
"""


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'None'
        return str(root.val) + ',' + str(self.serialize(root.left)) + ',' + str(self.serialize(root.right))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(',')
        return self.rdeserialize(data_list)

    def rdeserialize(self, data_list):
        if not data_list:
            return
        if data_list[0] == 'None':
            data_list.pop(0)
            return
        root = TreeNode(data_list[0])
        data_list.pop(0)
        root.left = self.rdeserialize(data_list)
        root.right = self.rdeserialize(data_list)

        return root