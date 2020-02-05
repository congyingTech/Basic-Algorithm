|  题目   | 描述  | 思路 |
|  -------  | ----  | ----|
| 01.reverse-linked-list  | 反转链表|三个指针:pre,cur,next |
| 02.merge-two-sorted-array  | 合并两个排序的数组|选择一个有序数组进行拓展，给两个有序数组的尾部分别一个指针，比较尾部的大小，把大的插入到拓展数组的尾部|
|03.merge-two-sorted-lists|合并两个排序的链表|比较第一个元素，小的为主链表，另一个为次链表，主链表两个指针，次链表一个指针，遍历次链表，插入到主链表| 
|04.subtree-of-another-tree|判断B是不是A的子树|递归的方法，判断两个树匹配的必要条件是:A.val==B.val and match(A.left, B.left) and match(A.right, B.right)，判断B是不是A的子树的条件是：全匹配match(A,B) or match(A.left, B) or match(A.right,B)|
|05.mirror-binary-tree|镜像二叉树|1)就地镜像：root.left, root.right = root.right, root.left; mirror(root.left); mirrot(root.right)  2)创建节点镜像：newTree=TreeNode(root.val);newTree.left = mirror(root.right);newTree.right = mirror(root.left)|
|06.print-matrix|顺时针打印矩阵|每次打印当前矩阵的第一行，然后将剩余的矩阵逆时针旋转90度|
|07.level-print-binary-tree|按层打印二叉树|队列|
|08.afteroder-level-tree-bst|根据后序遍历数组判断是不是二叉搜索树|后序遍历根左右，二叉搜索树根左<根<根右|
|09.copy-random-linkedlist|拷贝复杂链表|1)原复杂链表主体复制 2)复制复杂链表的灵活指针 3)把复制的链表从原链表脱离|
|10.bst-linkedlist-transfer|将bst树转化成有序的双向链表|递归的方法就左根右的遍历:左子树调整；调整左子树与根的关系；右子树调整|
|11.permutation|字符串全排列|回溯的思想|
|12.times-pass-half-of-all|出现过半数以上的num|摩尔投票法：times=1，遍历num，如果出现的话times+1，不出现的话times-1，如果是times==0的话，当前数字为新的比较数字，times重置为1，直到最后的那个数字|
|13.min-k-nums|找出k个小的数|利用最小堆的方法，每次建堆找出当前最小的元素，直到k次，时间复杂度是O(nlogk)|
|14.max-contiunus-arr-sum|连续子数组的最大和|dp[i]表示以i为连续数组最后一个元素的最大的和，dp[i] = max(dp[i-1]+num[i], num[i])|
|\*15.one-display-times|从1到n整数中1出现的次数|把从0到n的所有数分为几个部分，递归求解|
|16.arr-to-min-num|把数组排成最小的数|技巧题，用sort(cmp=lambda x,y:int(x+y)-int(y+x))|
|\*17.ugly-num|寻找第k个丑数|思路非常巧妙，看题目解析|
|18.first-char-one-time|第一个只出现一次的字符|dict|
|\*19.reverse-pair-in-arr|数组中的逆序对的数量|利用归并排序的特点，非常巧妙|
|20.two-list-first-common-node|两个链表的第一个公共结点|先遍历出两个链表的长度，较长的那个头指针先走一个长度差值，然后一起走，直到遇到公共结点|
|21.num-in-sortedarr-times|数字在排序数组中出现的次数|排序提醒了二分查找的方法，二分查找firstk和lastk出现的位置，然后做差值即可|
|22.tree-depth|二叉树的深度|dfs的方法，根据二叉树的深度延伸出来判断平衡二叉树的问题|
|\*23.arr-just-one-time-num|数组中只出现一次的数字|数组异或起来的结果就是x^y, 该题目考察了异或&和and &的用法|