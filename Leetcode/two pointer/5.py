#5. Longest Palindromic Substring
# Medium

# Given a string s, return the longest palindromic substring in s

#Example
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # expand two pointer sideways if it is still palindrome
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        # return string that are already palindrome
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''

        # move silding window one by one toward right side
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),  # check palindrome odd numbered
                         expand(i, i + 2),  # check palindrome even numbered
                         key=len)
        return result