"""
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。


解题思路：
动态规划：
dp[i]表示第i位时是否可以拆分成功，第i位字母是否可以拆分成功，取决于，前i-1位组成的字符串是否可以拆分成功，
前i-1位主要又包含从s[j:i-1]是否是dict中的一个单词 && s[0:j-1]是否可以拆分。
所以递推公式是：

dp[i] = dp[j] && check_in_dict[s[j:i-1]]

"""


class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                check_s = s[j:i]
                if dp[j] and check_s in wordDict:
                    dp[i] = True
                    break

        return dp[len(s)]


if __name__ == "__main__":
    s = Solution()
    st = "leetcode"
    wordDict = ["leet", "code"]
    print(s.wordBreak(st, wordDict))
