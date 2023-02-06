# 343. Integer Break
# Medium

# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
#
# Return the maximum product you can get.


# Example
# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0, 0, 1, 2, 4, 6, 9]
        if n < 7:
            return dp[n]

        dp += [0] * (n - 6)

        for i in range(7, n + 1):
            dp[i] = 3 * dp[i - 3]

        return dp[-1]