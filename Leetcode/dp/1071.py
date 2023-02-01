# 1071. Greatest Common Divisor of Strings
# Easy

# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
#
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


#Example
#Input                  Output
# 10 8                    1

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return str1[:math.gcd(len(str1), len(str2))] if str1 + str2 == str2 + str1 else ''
