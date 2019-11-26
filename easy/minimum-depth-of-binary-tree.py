#coding:utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def level_output(self, root):
        """
        层序遍历——按层输出
        :type root: TreeNode
        :rtype: int
        """
        root_res = [[root]]
        while root_res!=[[]]:
            root_l = root_res.pop()
            next_root = []
            print([r.val for r in root_l])
            for i in root_l:
                cur_root = i
                if cur_root.left:
                    next_root.append(cur_root.left)
                if cur_root.right:
                    next_root.append(cur_root.right)
            root_res.append(next_root)

    def minDepth(self, root):
        """
        只有叶子节点所在的层才能代表最小深度
        :type root: TreeNode
        :rtype: int
        """ 
        # 四种情况的讨论
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left and not root.right:
            return 1+self.minDepth(root.left)
        if root.right and not root.left:
            return 1+self.minDepth(root.right)
        left_depth = 1 + self.minDepth(root.left)
        right_depth = 1 + self.minDepth(root.right)

        return min(left_depth, right_depth)  




        
if __name__ == "__main__":
    # [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left= TreeNode(4)
    root.right= TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.left.right = TreeNode(7)
    s = Solution()
    s.level_output(root)

    res = s.minDepth(root)
    print(res)
