# 1155. Number of Dice Rolls With Target Sum
# Medium

# You have n dice, and each die has k faces numbered from 1 to k.
#
# Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice,
# so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

# Example:
# Input: n = 1, k = 6, target = 3
# Output: 1
# Explanation: You throw one die with 6 faces.
# There is only one way to get a sum of 3.

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        mod = 10 ** 9 + 7

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                m = 1
                while m <= min(j, k):
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - m]) % mod
                    m += 1
        return dp[n][target] % mod
