### 动态规划专题

> 动态规划专题魔鬼训练营，start from 20210104

|  题目   | 描述  | 思路 | 归类 | 解题时间 |
|  ----  | ----  | ---- | ---- | ---- |
|338.counting-bits|比特位计数|-|动态规划|2021-01-04|
|139.word-break|单词拆分|dp[i]表示第i位时，是否可以被拆分，dp[i]是否可以被拆分取决于0:j组成的字符串是否可以被拆分以及s[j:i-1]在wordDict中，所以递推表达式是dp[i] = dp[j] && check_s_in_dict(s[i:j-1]), 初始化的dp[0]=True |动态规划|2021-01-25|
|62.|
|309.|
|5.|
