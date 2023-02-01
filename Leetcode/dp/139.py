#139. Word Break
# Medium

# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.


#Example
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s) + 1):
                if dp[j] and s[i:j] in wordDict:
                    dp[i] = True
                    break

        return dp[0]