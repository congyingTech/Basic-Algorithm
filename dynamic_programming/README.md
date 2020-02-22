### 动态规划专题

|  题目   | 描述  | 思路 | 
|  ----  | ----  | ---- | 
|1.ugly-number.py|寻找第k个丑数|略|
|2.program-for-nth-fibonacci-number.py|斐波那契数列|略|
|3.bell-numbers-number-of-ways-to-partition-a-set.py|Bell数(n长度的数，随意分割，有多少分割方法)|假设n是长度，k是partition个数，S(n,k)是n长度分割成k个partition的数目，第n个数可以独自成为一个partition，也可以放入到前几个partition中，所以S(n,k)=k*S(n-1,k) + S(n-1, k-1), 那么k属于(0,n), n长度的数总共有S(n,0)+...S(n,k)..+S(n,n)，其中S(n,0)=S(n,n)=1|
|4.binomial-coefficient.py|组合数|C(n,k) = C(n-1,k-1) + C(n-1,k)|
|5.permutation-coefficient.py|排列数|A(n,k)=n*A(n-1,k-1)|
|6.tiling-problem.py|地板填充(2*n大小被2*1大小的填充，有多少种填充方案)|2*1的地板只能横放和竖放，如果横放，占n的两个格，如果竖放，占n的一个格，dp(n)是n*2大小的地板有多少种铺设方案，那么dp(n) = dp(n-2) + dp(n-1)|
|7.gold-mine-problem.py|最大黄金量|dp[i][j] = max(dp[i+1][j-1], dp[i][j-1], dp[i-1][j-1]) + w[i][j]|
|8.coin-change.py|有m个面值分别是Sm的硬币，求问组成N元钱的可能的组合个数？|第m个硬币有两种情况，至少包含一个m硬币才能组成N元，不包含任何m硬币不组成N元，所以count(N,m)表达的是第m个硬币组成N元的个数，count(N,m) = count(N, m-1)+count(N-Sm, m)|
|9.coin-change2.py|有m个面值是Sm的硬币，组合成N元钱的最少的硬币数？|第m个硬币选择或者不选择，min_count(N,m) = min(min_count(N-Sm, m))+ 1, min_count(N, m-1))|
|10.friends-pairing-problem.py|给定n个朋友，朋友可以单身也可以两两配对，求这样的组合的可能个数。|f(n)表示第n个人的时候有多少的组合数，第n个人可以单身，这样的话f(n)=f(n-1)，第n个人可以从前n-1个人中选一个人配对，这样f(n)=(n-1)*f(n-2)，所以f(n) = f(n-1) + (n-1)*f(n-2)|
|11.subset-sum-problem.py|给定一组非负整数nums，和一个和值k，求问能等于和值的数组子集组合是否存在|对于第n个数，有两种情况，组成和值，不组成和值，如果前n-1个和值已经是k了，那么第n个数也是True，如果前n-1组成的和值个是k-nums[n]，那么第n个数返回也是True，所以f(n,k)是第n个数是否能组成k，f(n,k) = f(n-1,k) or f(n-1,k-nums[n])|
|12.encoding-ways.py|编码方式的个数（A～Z对应着0～25，给定一个数字字符串，求这个字符串对应几种字母编辑方式，例如：0219可以是ACBJ或者ACX或者AZJ，三种编码方式）|对于给定的数字的第n位数，f(n)表示n位数编码方式的个数，有两种情况，单独成为一个字母f(n) = f(n-1)，或者当满足和前一个大于0小于3的数组合成20～26的字母，此时，f(n)=f(n-1)+f(n-2)|
|13.subset-sum-divisible-m.py|子集的和是否可以被m整除|subset-sum-problem的变种|
|14.largest-divisible-pairs-subset.py|||
|15.LISLength.py|最长上升子序列|对于第n个数如果比前n-1个组成的最长上升子序列的最后一个值大，那么加入，否则不加入，f(n)是n长度的list组成的最长上升子序列f(n) = max(f(j)+1, f(n))其中0<=j<=n-1且list[n]>list[j]|
|16.LCSLength.py|最长公共子序列|假设包含A的第m个元素和B的第n个元素时，最长公共子序列是L(m,n),如果A的第m个元素等于B的第n个元素，那么L(m,n) = L(m-1,n-1)+1; 否则L(m,n)=max(L(m,n-1), L(m-1,n))|
