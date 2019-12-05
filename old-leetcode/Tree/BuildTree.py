class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def buildTree(nums1, nums2):
    root = TreeNode(nums1[0])
    n = len(nums2)
    m = len(nums1)
    if n == 0 and m == 0:  # 当两者都为0的时候停止递归
        return None
    indInNums2 = nums2.index(nums1[0])  # 寻找根结点在nums2中的位置， nums1中的第一个元素总是根结点
    leftTreeList = [nums2[i] for i in range(indInNums2)]  # nums2确定左子树
    lenLeftTree = len(leftTreeList)  # 左子树的长度
    rightTreeList = [nums2[j] for j in range(indInNums2 + 1, n)]  # nums2确定右子树
    lenRightTree = len(rightTreeList)  # 右子树的长度
    if lenLeftTree != 0:
        root.left = buildTree(nums1[1: 1 + lenLeftTree], leftTreeList)
    if lenRightTree != 0:
        root.right = buildTree(nums1[1 + lenLeftTree:], rightTreeList, )
    return root


def bianli(root):  # 前序遍历
    if root == None:
        return
    print(root.value)
    bianli(root.left)
    bianli(root.right)


if __name__ == "__main__":
    nums1 = [1, 2, 4, 7, 3, 5, 6, 8]  # 前序遍历：根左右
    nums2 = [4, 7, 2, 1, 5, 3, 8, 6]  # 中序遍历：左根右
    builtroot = buildTree(nums1, nums2)
    bianli(builtroot)
