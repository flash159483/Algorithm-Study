# 583. Delete Operation for Two Strings
# Medium

# Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
#
# In one step, you can delete exactly one character in either string.

# Example
# Input: word1 = "sea", word2 = "eat"
# Output: 2
# Explanation: You need one step to

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        max_len = dp[-1][-1]

        return (len(word1) - max_len) + (len(word2) - max_len)