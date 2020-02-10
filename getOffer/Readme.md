### 剑指Offer题解

> 16题之前比较基础，后续再更新


|  题目   | 描述  | 思路 | 归类 | 解题时间 |
|  ----  | ----  | ---- | ---- | ---- |
|03.search-in-matrix|二维数组的查找|从右上角开始，右上角的值大于查找的数字则删除所在列，小于则删除所在的行，直到找到位置|数组|2020-2-10|
|05.reverse-print-linkedlist|从尾到头打印链表|遍历一遍+stack|链表|2020-2-10|
|[06.rebuild-binary-tree](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/06.rebuild-binary-tree.py)|重建二叉树|根据前序和中序遍历结果重建|二叉树|2020-2-10|
|08.trans-matrix-min|旋转数组的最小数字|二分搜索的方法，start，end，mid，如果start的值小于mid的值，说明start-mid之间是递增的数组，最小值在mid-end之间，如果start的值大于mid，说明mid处于后面的递增数组，而最小值就在start-mid之间|二分查找|2020-2-10|
|10.one-times|二进制中1的个数|让n每次位与n-1，n-1相当于n左移动一位，相当于看除了第一位之外的1的个数，每次n=n&(n-1),count+=1那么直到n=0的时候，结束|位运算|2020-2-10|
|13.delete-node-in-linkedlist|在O(1)时间删除链表的结点|将后一个结点的值复制给p，删除p.next结点|链表|2020-2-10|
|14.odd-even|调整数组使奇数在前偶数在后|头尾双指针|双指针|2020-2-10|
|15.k-num-in-linkedlist|链表中倒数第k个结点|快慢指针|双指针|2020-2-10|
|[16.reverse-linked-list](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/16.reverse-linked-list.py)| 反转链表|三个指针:pre,cur,next |链表| 2020-1-31 |
|[17.merge-two-sorted-array](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/17.merge-two-sorted-array.py)| 合并两个排序的数组|选择一个有序数组进行拓展，给两个有序数组的尾部分别一个指针，比较尾部的大小，把大的插入到拓展数组的尾部 | 有序数组排序 | 2020-1-31 |
|[17.merge-two-sorted-lists](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/17.merge-two-sorted-lists.py)|合并两个排序的链表|比较第一个元素，小的为主链表，另一个为次链表，主链表两个指针，次链表一个指针，遍历次链表，插入到主链表|有序链表排序| 2020-1-31 |
|[18.subtree-of-another-tree](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/18.subtree-of-another-tree.py)|判断B是不是A的子树|递归的方法，判断两个树匹配的必要条件是:A.val==B.val and match(A.left, B.left) and match(A.right, B.right)，判断B是不是A的子树的条件是：全匹配match(A,B) or match(A.left, B) or match(A.right,B)|二叉树|2020-1-31 |
|[19.mirror-binary-tree](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/19.mirror-binary-tree.py)|镜像二叉树|1)就地镜像：root.left, root.right = root.right, root.left; mirror(root.left); mirrot(root.right)  2)创建节点镜像：newTree=TreeNode(root.val);newTree.left = mirror(root.right);newTree.right = mirror(root.left)|二叉树|2020-1-31 |
|[20.print-matrix](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/20.print-matrix.py)|顺时针打印矩阵|每次打印当前矩阵的第一行，然后将剩余的矩阵逆时针旋转90度|数组|2020-1-31 |
|[23.level-print-binary-tree](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/23.level-print-binary-tree.py)|按层打印二叉树|队列|队列-先进先出|2020-1-31 |
|[24.afterorder-level-tree-bst](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/24.afterorder-level-tree-bst.py)|根据后序遍历数组判断是不是二叉搜索树|后序遍历根左右，二叉搜索树根左<根<根右|二叉树遍历|2020-1-31 |
|[26.copy-random-linkedlist](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/26.copy-random-linkedlist.py)|拷贝复杂链表|1)原复杂链表主体复制 2)复制复杂链表的灵活指针 3)把复制的链表从原链表脱离|链表|2020-2-2|
|[27.bst-linkedlist-transfer](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/27.bst-linkedlist-transfer.py)|将bst树转化成有序的双向链表|递归的方法就左根右的遍历:左子树调整；调整左子树与根的关系；右子树调整|双向链表和树|2020-2-2|
|[28.permutation](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/28.permutation.py|字符串全排列|回溯的思想|回溯|2020-2-2|
|[29.times-pass-half-of-all](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/29.times-pass-half-of-all.py)|出现过半数以上的num|摩尔投票法：times=1，遍历num，如果出现的话times+1，不出现的话times-1，如果是times==0的话，当前数字为新的比较数字，times重置为1，直到最后的那个数字|快排+数学|2020-2-2|
|[30.min-k-nums](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/30.min-k-nums.py)|找出k个小的数|利用最小堆的方法，每次建堆找出当前最小的元素，直到k次，时间复杂度是O(nlogk)|堆|2020-2-4|
|[31.max-contiunus-arr-sum](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/31.max-contiunus-arr-sum.py)|连续子数组的最大和|dp[i]表示以i为连续数组最后一个元素的最大的和，dp[i] = max(dp[i-1]+num[i], num[i])|动态规划|2020-2-4|
|[\*32.one-display-times](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/32.one-display-times.py)|从1到n整数中1出现的次数|把从0到n的所有数分为几个部分，递归求解|递归|2020-2-4|
|[33.arr-to-min-num](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/33.arr-to-min-num.py)|把数组排成最小的数|技巧题，用sort(cmp=lambda x,y:int(x+y)-int(y+x))|数组|2020-2-4|
|[\*34.ugly-num](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/34.ugly-num.py)|寻找第k个丑数|思路非常巧妙，看题目解析|空间换时间|2020-2-4|
|[35.first-char-one-time](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/35.first-char-one-time.py)|第一个只出现一次的字符|dict|map|2020-2-4|
|[\*36.reverse-pair-in-arr](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/36.reverse-pair-in-arr.py)|数组中的逆序对的数量|利用归并排序的特点，非常巧妙|归并排序|2020-2-5|
|[37.two-list-first-common-node](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/37.two-list-first-common-node.py)|两个链表的第一个公共结点|先遍历出两个链表的长度，较长的那个头指针先走一个长度差值，然后一起走，直到遇到公共结点|双指针|2020-2-5|
|[38.num-in-sortedarr-times](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/38.num-in-sortedarr-times.py)|数字在排序数组中出现的次数|排序提醒了二分查找的方法，二分查找firstk和lastk出现的位置，然后做差值即可|二分查找|2020-2-5|
|[39.tree-depth](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/39.tree-depth.py)|二叉树的深度|dfs的方法，根据二叉树的深度延伸出来判断平衡二叉树的问题|DFS|2020-2-5|
|[\*40.arr-just-one-time-num](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/40.arr-just-one-time-num.py)|数组中只出现一次的数字(数组中两个数是出现了一次，其余数均出现两次)|数组异或起来的结果就是x^y, 该题目考察了异或&和and &的用法|位运算|2020-2-5|
|[41.sum-target-num-arr](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/41.sum-target-num-arr.py)|和为s的两个数字 vs 和为s的连续正数序列|大小指针的思路|双指针|2020-2-5|
|[42.reverse-word-vs-left-trans-string](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/42.reverse-word-vs-left-trans-str.py)|翻转单词顺序 vs 左旋转字符串|整体翻转句子顺序，然后对每次单词进行翻转|字符串|2020-2-5|
|[43.n-probability](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/43.n-probability.py)|n个骰子的点数|用递归和数组的思想解决|数学|2020-2-6|
|[44.IsContinuous](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/44.IsContinuous.py)|扑克牌的顺子|排序，看是否是顺子|排序|2020-2-6|
|[45.circle-last-num](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/45.circle-last-num.py)|圆圈中最后剩下的数字|循环链表|链表删除结点|2020-2-6|
|[46.1-n-sum](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/46.1-n-sum.py)|求1+2+...+n|递归的方法求解|递归|2020-2-6|
|[47.sum-way](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/47.sum-way.py)|不用加减乘除法做加法|两个数做异或和位与，并将结果继续异或和位与，直到位与的结果是0.|位运算|2020-2-6|
|[49.str-to-int](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/49.str-to-int.py)|字符数字转化成int|利用字符的ascii码，‘0’的ascii码是48，那么其他的减去48即int数值|字符串|2020-2-6|
|[50.two-nodes-last-father](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/50.two-nodes-last-father.py)|树中两个结点的公共祖先|分为几种情况：二叉搜索树/普通二叉树/多叉树|二叉树|2020-2-7|
|[\*51.repeat-num-in-arr](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/51.repeat-num-in-arr.py)|数组中重复的数字|巧用数字的值大小在0～n-1之间，通过将数字归位，寻找重复数字|数组|2020-2-7|
|[\*52.build-mult-arr](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/52.build-mult-arr.py)|构建乘积数组|将A分为左右两部分，这样时间复杂度是O(N)|数组|2020-2-7|
|[53.regular-match](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/53.regular-match.py)|正则表达式匹配|比较工程的一个题目|字符串|2020-2-7|
|[56.entrance-in-circle-linkedlist](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/56.entrance-in-circle-linkedlist.py)|链表中环的入口|快慢指针(找出链表环的长度n)+双指针(p1先走n步，然后p1和p2再相遇的时候就是环入口结点)|双指针|2020-2-9|
|[57.delete-repeat-node-in-linkedlist](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/57.delete-repeat-node-in-linkedlist.py)|删除链表中所有的重复元素|三个指针|链表|2020-2-9|
|[58.binary-tree-next-node](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/58.binary-tree-next-node.py)|二叉树的下一个结点|三种情况：当前结点有右子树，那么返回右子树的最左结点；当前结点没有右子树，且当前结点处于父结点的左子树上，那么返回父节点；当前结点没有右子树也不在父节点的左子树上，那么向上回溯，直到找到这么一个满足在父节点的左子树上的父节点。|二叉树|2020-2-9|
|[59.symmetric-tree](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/59.symmetric-tree.py)|对称二叉树|1)递归：两棵树，看左右子树是否相同 2)非递归：BFS+stack|二叉树|2020-2-9|
|60.level-print-binary-tree|把二叉树打印成多行|第7题已经写出了按层打印二叉树的解法|二叉树层序遍历|2020-2-9|
|61.level-print-binary-tree|按之字形顺序打印二叉树|还是按层遍历二叉树的变种，不再赘述|二叉树层序遍历|2020-2-9|
|[\*62.serial-binary-tree](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/62.serial-binary-tree.py)|序列化二叉树|可以根据前序遍历，把null补充为‘$’，然后从根结点开始重构二叉树，通过把前序遍历的结果放在一个iter里面，每次迭代出来的结果就是左孩子，左孩子|二叉树|2020-2-10|
|63.bst-k-num|二叉搜索树的第k大结点|bst树的中序遍历是有序的，所以中序遍历，然后找到第k个元素(递归，非递归)|BST树|2020-2-9|
|[\*64.data-stream-middle-num](https://github.com/congyingTech/Basic-Algorithm/blob/master/data_structure/7.heap.py)|数据流的中位数|如果排过序的数组，很容易找到中位数，而对于数据流，并不知道下一个数字是什么，所以可以用堆的思路，分为左右两个堆，左堆是最大堆，右堆是最小堆，左堆的数字都比右堆小，左堆的最大值和右堆的最小值的平均是中位数。堆的分配保证均衡，通过奇数往左堆(最大堆)放，偶数往右堆插入(最小堆)。那么还有一个问题，就是如果新插入左堆(最大堆)的数字比右堆(最小堆)最小的数字还大，那么将该数先插入右堆，pop出右堆最小的数字插入到左堆；镜像：如果新插入右堆(最小堆)的数字比左堆(最大堆)的最大值还小，那么将该数插入左堆，pop出左堆的最大数字插入到右堆。当所有的数字都建堆完毕了，那么左右堆的top值就是中位数。时间复杂度是建堆的时间复杂度O(logN)|堆|2020-2-10|
|[\*65.sliding-window-maximum](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/65.sliding-window-maximum.py)|滑动窗口的最大值|双端队列保存最大值和次大值|双端队列|2020-2-10|
|[66.matrix-path](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/66.matrix-path.py)|矩阵中的路径|判断一个路径是否存在在矩阵中，可以用回溯法|回溯法|2020-2-10|
|[\*67.robot-fields](https://github.com/congyingTech/Basic-Algorithm/blob/master/getOffer/67.robot-fields.py)|机器人运动范围|寻找机器人可以活动的board|回溯法|2020-2-10|

