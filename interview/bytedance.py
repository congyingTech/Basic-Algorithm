class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def transfer(self, root):
        if not root:
            return
        self.transfer(root.left)
        if self.head==None and self.tail == None:
            self.head, self.tail = root, root
        else:
            self.tail.right = root
            root.left = self.tail
            self.tail = self.tail.right
        self.transfer(root.right)
        return self.head

if __name__ == "__main__":
    s = Solution()
    root = None
    s.transfer(root)