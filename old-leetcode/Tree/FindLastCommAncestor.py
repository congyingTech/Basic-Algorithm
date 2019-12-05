class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value= value

"""
假设树是搜索二叉树，树的左子树都比根节点小， 树的右子树都比根节点大
"""
def findNearestAncestor(root, node1, node2):
    if node1.value > root.value and node2.value > root.value: # 两个node都比根节点大，那么公共最近祖先在右子树，对右子树进行递归
        return findNearestAncestor(root.right, node1, node2)
    elif node1.value < root.value and node2.value < root.value:
        return findNearestAncestor(root.left, node1, node2)
    else:
        return root


"""
假设树是普通二叉树，那么判断x1和x2是否分别在左右子树中，如果是的，那么该节点就是公共祖先，如果x1， x2都在左子树，递归左子树，否则递归右子树
"""
def findLastCommAncestor(root, node1, node2):
    if root==node1 or root==node2:
        return root
    node1inleft = Judge(root.left, node1)
    print(node1inleft)
    node1inright = Judge(root.right, node1)
    print(node1inright)
    node2inleft = Judge(root.left, node2)
    print(node2inleft)
    node2inright = Judge(root.right, node2)
    print(node2inright)
    if node1inleft and node2inleft:
        findNearestAncestor(root.left, node1, node2)
    elif node1inright and node2inright:
        findNearestAncestor(root.right, node1, node2)
    else:
        return root

def Judge(root, node, result = False):
    if root == None:
        return
    if node.value == root.value:
        result = True
    Judge(root.left, node)
    Judge(root.right, node)
    return result


def bianli(root):
    if root == None:
        return
    print(root.value)
    bianli(root.left)
    bianli(root.right)

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(0)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    root.right.right.right = TreeNode(9)

    #bianli(root)
    node1 = TreeNode(4)
    node2 = TreeNode(9)
    result1 = findLastCommAncestor(root, node1, node2)
    print(result1.value)