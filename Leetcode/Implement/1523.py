# 1523. Count Odd Numbers in an Interval Range
# Easy

# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

# Example
# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            return (high - low  + 1) // 2
        return (high - low) // 2 + 1