# 67. Add Binary
# Silver 1

# Given two binary strings a and b, return their sum as a binary string.

# Example
# Input: a = "11", b = "1"
# Output: "100"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result, carry = '', 0
        arr_A = list(a)
        arr_B = list(b)
        while arr_A or arr_B or carry:
            if arr_A:
                carry += int(arr_A.pop())
            if arr_B:
                carry += int(arr_B.pop())

            result += str(carry % 2)
            carry //= 2
        return result[::-1]