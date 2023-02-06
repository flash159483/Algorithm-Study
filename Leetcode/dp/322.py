# 322. Coin Change
# Medium

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.


# Example
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[sys.maxsize]*(amount+1) for _ in range(len(coins))]

        for c in range(len(coins)):
            dp[c][0] = 0
            for i in range(1, amount+1):

                dp[c][i] = dp[c-1][i]
                if i >= coins[c]:
                    dp[c][i] = min(dp[c][i], dp[c][i-coins[c]]+1)

        return dp[len(coins)-1][amount] if dp[len(coins)-1][amount] != sys.maxsize else -1