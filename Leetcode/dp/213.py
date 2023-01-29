#213. House Robber II
#Medium
#
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
# All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
# Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
# Example
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(left, right):
            dp = [0] * 100
            dp[left] = nums[left]
            dp[left + 1] = max(nums[left], nums[left + 1])

            for i in range(left + 2, right):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

            return max(dp)

        if len(nums) <= 2:
            return max(nums)
        #to avoid robbing the first and last house rob the house from 0->n-1 and 1->n 
        return max(solve(0, len(nums) - 1), solve(1, len(nums)))