# 70. Climbing Stairs
# Easy

# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

class Solution:
    dp = collections.defaultdict(int)

    def climbStairs(self, num: int) -> int:
        if num <= 2:
            return num

        if self.dp[num]:
            return self.dp[num]

        self.dp[num] = self.climbStairs(num - 1) + self.climbStairs(num - 2)
        return self.dp[num]