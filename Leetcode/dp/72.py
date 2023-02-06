# 72. Edit Distance
# Medium

# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
#
# You have the following three operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character


# Example
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                # word1 have no character to become word2[:j] you have insert all of it
                if i == 0:
                    dp[i][j] = j
                # word2 have no character to become word2 you have to delete all of word1[:i]
                elif j == 0:
                    dp[i][j] = i

                # since the char is same no need to delete or insert just carry on
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # get min operation of delete, insert, replace all need 1 operation
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        return dp[len(word1)][len(word2)]