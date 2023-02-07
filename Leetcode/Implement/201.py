# 201. Bitwise AND of Numbers Range
# Medium

# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.


# Example
# Input: left = 5, right = 7
# Output: 4

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while left != right:
            left >>= 1
            right >>= 1
            i += 1
        return right << i
