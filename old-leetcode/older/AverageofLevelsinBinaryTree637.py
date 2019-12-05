# Definition for a binary tree node.
#寻找每一层的平均值
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #利用队列实现层序遍历
    def averageOfLevels(self, root):
        if root == None:
            return 
        ans = []
        que = [root]
        index = 0
        print('0 level:%d'%que[0].val)
        while que:
            ans.append( 1.0*sum ([i.val for i in que])/len(que))
            nque = []#每一层的数据
            for n in que:
                if n.left: nque.append(n.left)   
                if n.right: nque.append(n.right) 
            index+=1
            print('%d level: %s'%(index,' '.join([str(i.val) for i in nque])))
            que = nque 
        return ans
        

if __name__ == '__main__':
    root =   TreeNode(3)
    root.left = TreeNode(9)
    root.left.left = TreeNode(2)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7) 
    print(Solution().averageOfLevels(root))
