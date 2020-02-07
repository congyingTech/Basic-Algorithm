### 剑指Offer题解

> 16题之前比较基础，后续再更新


|  题目   | 描述  | 思路 | 解题时间 |
|  ----  | ----  | ---- | ---- |
| 01.reverse-linked-list  | 反转链表|三个指针:pre,cur,next | 2020-1-31 |
| 02.merge-two-sorted-array  | 合并两个排序的数组|选择一个有序数组进行拓展，给两个有序数组的尾部分别一个指针，比较尾部的大小，把大的插入到拓展数组的尾部| 2020-1-31 |
|03.merge-two-sorted-lists|合并两个排序的链表|比较第一个元素，小的为主链表，另一个为次链表，主链表两个指针，次链表一个指针，遍历次链表，插入到主链表| 2020-1-31 |
|04.subtree-of-another-tree|判断B是不是A的子树|递归的方法，判断两个树匹配的必要条件是:A.val==B.val and match(A.left, B.left) and match(A.right, B.right)，判断B是不是A的子树的条件是：全匹配match(A,B) or match(A.left, B) or match(A.right,B)|2020-1-31 |
|05.mirror-binary-tree|镜像二叉树|1)就地镜像：root.left, root.right = root.right, root.left; mirror(root.left); mirrot(root.right)  2)创建节点镜像：newTree=TreeNode(root.val);newTree.left = mirror(root.right);newTree.right = mirror(root.left)|2020-1-31 |
|06.print-matrix|顺时针打印矩阵|每次打印当前矩阵的第一行，然后将剩余的矩阵逆时针旋转90度|2020-1-31 |
|07.level-print-binary-tree|按层打印二叉树|队列|2020-1-31 |
|08.afteroder-level-tree-bst|根据后序遍历数组判断是不是二叉搜索树|后序遍历根左右，二叉搜索树根左<根<根右|2020-1-31 |
|09.copy-random-linkedlist|拷贝复杂链表|1)原复杂链表主体复制 2)复制复杂链表的灵活指针 3)把复制的链表从原链表脱离|2020-2-2|
|10.bst-linkedlist-transfer|将bst树转化成有序的双向链表|递归的方法就左根右的遍历:左子树调整；调整左子树与根的关系；右子树调整|2020-2-2|
|11.permutation|字符串全排列|回溯的思想|2020-2-2|
|12.times-pass-half-of-all|出现过半数以上的num|摩尔投票法：times=1，遍历num，如果出现的话times+1，不出现的话times-1，如果是times==0的话，当前数字为新的比较数字，times重置为1，直到最后的那个数字|2020-2-2|
|13.min-k-nums|找出k个小的数|利用最小堆的方法，每次建堆找出当前最小的元素，直到k次，时间复杂度是O(nlogk)|2020-2-4|
|14.max-contiunus-arr-sum|连续子数组的最大和|dp[i]表示以i为连续数组最后一个元素的最大的和，dp[i] = max(dp[i-1]+num[i], num[i])|2020-2-4|
|\*15.one-display-times|从1到n整数中1出现的次数|把从0到n的所有数分为几个部分，递归求解|2020-2-4|
|16.arr-to-min-num|把数组排成最小的数|技巧题，用sort(cmp=lambda x,y:int(x+y)-int(y+x))|2020-2-4|
|\*17.ugly-num|寻找第k个丑数|思路非常巧妙，看题目解析|2020-2-4|
|18.first-char-one-time|第一个只出现一次的字符|dict|2020-2-4|
|\*19.reverse-pair-in-arr|数组中的逆序对的数量|利用归并排序的特点，非常巧妙|2020-2-5|
|20.two-list-first-common-node|两个链表的第一个公共结点|先遍历出两个链表的长度，较长的那个头指针先走一个长度差值，然后一起走，直到遇到公共结点|2020-2-5|
|21.num-in-sortedarr-times|数字在排序数组中出现的次数|排序提醒了二分查找的方法，二分查找firstk和lastk出现的位置，然后做差值即可|2020-2-5|
|22.tree-depth|二叉树的深度|dfs的方法，根据二叉树的深度延伸出来判断平衡二叉树的问题|2020-2-5|
|\*23.arr-just-one-time-num|数组中只出现一次的数字(数组中两个数是出现了一次，其余数均出现两次)|数组异或起来的结果就是x^y, 该题目考察了异或&和and &的用法|2020-2-5|
|24.sum-target-num-arr|和为s的两个数字 vs 和为s的连续正数序列|大小指针的思路|2020-2-5|
|25.reverse-word-vs-left-trans-string|翻转单词顺序 vs 左旋转字符串|整体翻转句子顺序，然后对每次单词进行翻转|2020-2-5|
|26.n-probability|n个骰子的点数|用递归和数组的思想解决|2020-2-6|
|27.IsContinuous|扑克牌的顺子|排序，看是否是顺子|2020-2-6|
|28.circle-last-num|圆圈中最后剩下的数字|循环链表|2020-2-6|
|29.1-n-sum|求1+2+...+n|递归的方法求解|2020-2-6|
|30.sum-way|不用加减乘除法做加法|两个数做异或和位与，并将结果继续异或和位与，直到位与的结果是0.|2020-2-6|
|31.str-to-int|字符数字转化成int|利用字符的ascii码，‘0’的ascii码是48，那么其他的减去48即int数值|2020-2-6|
|32.two-nodes-last-father|树中两个结点的公共祖先|分为几种情况：二叉搜索树/普通二叉树/多叉树|2020-2-7|
|\*33.repeat-num-in-arr|数组中重复的数字|巧用数字的值大小在0～n-1之间，通过将数字归位，寻找重复数字|2020-2-7|
|\*34.build-mult-arr|构建乘积数组|将A分为左右两部分，这样时间复杂度是O(N)|2020-2-7|
|35.regular-match|正则表达式匹配|比较工程的一个题目|2020-2-7|
