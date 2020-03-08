# encoding:utf-8
"""
问题描述：二叉搜索树与双向链表，二叉搜索树转化成一个排序的双向链表
解决方案：
1）递归:把问题分解成把左子树调成双向链表，把根与左(右)子树调成双向链表，调整右子树
2）非递归：二叉搜索树的中序遍历就是从小到大的排序，用一个stack记录二叉搜索树的中序遍历，然后pop出来的节点进行连接
"""
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution1(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def transfer(self, root):
        if not root:
            return 
        # 整理好的左子树
        self.transfer(root.left)
        if self.head==None and self.tail == None:
            self.head, self.tail = root, root
        else:
            # 将self.tail与根节点双向链接，且self.tail向后移动一步，A->B 双向链接后，A指向B
            self.tail.right = root
            root.left = self.tail
            self.tail = self.tail.right
        # 整理右子树
        self.transfer(root.right)
        return self.head

    def printList(self, head):
        while head.right:
            print(head.val)
            head = head.right
        print(head.val)
        while head:
            print(head.val)
            head = head.left

class Solution2(object):
    def transfer(self, root):
        stack = [root]
        res = []
        head = root
        while head:
            if head.left and head.left not in res:
                stack.append(head.left)
                res.append(head.left)
                head = head.left
            elif len(stack)>2:
                last_node = stack.pop()
                next_node = stack[-1]
                if not last_node.right == next_node:
                    last_node.right = next_node
                if not next_node.left==last_node:
                    next_node.left = last_node
                head = next_node
            elif head.right and head.right not in res:
                stack.append(head.right)
                res.append(head.right)
                head = head.right
            else:
                break
        return last_node


if __name__ == "__main__":
    s = Solution1()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(6)
    head = s.transfer(root)
    s.printList(head)
