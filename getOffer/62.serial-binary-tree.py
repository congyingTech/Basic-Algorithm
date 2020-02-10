# encoding:utf-8
class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def Serialize(self, root):
        # write code here
        vallist = []
        def preOrder(root):
            if not root:
                vallist.append('#')
            else:
                vallist.append(str(root.val))
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        return ' '.join(vallist)
    def Deserialize(self, s):
        # write code here
        vallist = iter(s.split())   
        # 利用分隔好的字符串生成的数组生成一个迭代器。可以不断被next调用，每调用一次他就会返回下一个元素。
        def dePre():
            val = next(vallist)  # 通过next不断调用vallist这个迭代器里的元素，相当于for循环。
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = dePre()
            node.right = dePre()
            return node
        return dePre()

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    string = s.Serialize(root)
    r = s.Deserialize(string)
    print(r)