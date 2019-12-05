class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        root = TreeNode(pre[0])
        n = len(tin);
        m = len(pre)
        if n == 0 and m == 0:  # 当两者都为0的时候停止递归
            return None
        indInNums2 = tin.index(pre[0])  # 寻找根结点在nums2中的位置， nums1中的第一个元素总是根结点
        leftTreeList = [tin[i] for i in range(indInNums2)]  # nums2确定左子树
        lenLeftTree = len(leftTreeList)  # 左子树的长度
        rightTreeList = [tin[j] for j in range(indInNums2 + 1, n)]  # nums2确定右子树
        lenRightTree = len(rightTreeList)  # 右子树的长度
        if lenLeftTree != 0:
            root.left = self.reConstructBinaryTree(pre[1: 1 + lenLeftTree], leftTreeList)
        if lenRightTree != 0:
            root.right = self.reConstructBinaryTree(pre[1 + lenLeftTree:], rightTreeList)
        return root

def bianli(root):  # 前序遍历
    if root == None:
        return
    print(root.val)
    bianli(root.left)
    bianli(root.right)

if __name__ == "__main__":
    s = Solution()

    nums1 = [1, 2, 4, 7, 3, 5, 6, 8]  # 前序遍历：根左右
    nums2 = [4, 7, 2, 1, 5, 3, 8, 6]  # 中序遍历：左根右
    root = s.reConstructBinaryTree(nums1, nums2)
    bianli(root)