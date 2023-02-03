# 673. Number of Longest Increasing Subsequence
# Medium

# Given an integer array nums, return the number of longest increasing subsequences.
#
# Notice that the sequence has to be strictly increasing.

# Example
# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[1, 1] for i in range(len(nums))]
        result = 1
        for i in range(len(nums)):
            max_len, count = 1, 0
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j][0] >= max_len:
                        max_len = dp[j][0] + 1
                        count = 0
                    if dp[j][0] == max_len - 1:
                        count += dp[j][1]
            dp[i] = [max_len, max(count, dp[i][1])]
            result = max(max_len, result)
        return sum([i[1] for i in dp if i[0] == result])