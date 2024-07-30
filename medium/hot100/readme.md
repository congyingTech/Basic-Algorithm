### LeetCode题解-Hot标签题解

|  题目   | 描述  | 思路 | 归类 | 解题时间 |
|  ----  | ----  | ---- | ---- | ---- |
|hot100/23-merge-k-sorted-lists.py| 合并k个排序的链表|在合并两个排序的链表的基础上，分治法|链表|2021-07-06|
|hot100/*42-trapping-rain-water.py| 一些柱子，这些柱子能接多少水？（注意和11题的区分,这个有宽度为1）|动态规划+双指针|动态规划|2021-07-06|
|hot100/11-container-with-most-water.py| 盛最多水的容器|动态规划+双指针:if height[left]<height[right]: left+=1 else:right-=1, max_area = max(min(height[l], height[r])*(r-l))|动态规划|2021-07-06|
|hot100/70-climbing-stairs.py| 爬楼梯|-|动态规划|2021-07-06|
|hot100/*10-regular-expression-matching.py|正则化匹配|dp[i][j]表示s的前i个字符和p的前j个字符可以match,情况1）p当前位置是字符或者是.；情况2）p当前位置是*|动态规划
