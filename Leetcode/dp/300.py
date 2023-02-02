# 300. Longest Increasing Subsequence
# Medium

# Given an integer array nums, return the length of the longest strictly increasing subsequence.

#Example
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        dp = [0] * 2500
        for i in range(len(arr)):
            for j in range(i):
                if arr[i] > arr[j] and dp[i] < dp[j]:
                    dp[i] = dp[j]
            dp[i] += 1

        return max(dp)

