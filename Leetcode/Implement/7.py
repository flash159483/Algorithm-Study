# 7. Reverse Integer
# Medium

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example
# Input: x = 123
# Output: 321


class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:
            tmp = str(-x)
            tmp = -int(tmp[::-1])
        else:
            tmp = str(x)
            tmp = int(tmp[::-1])

        if not -2 ** 31 <= tmp <= 2 ** 31 - 1:
            return 0

        return tmp