# 567. Permutation in String
# Medium

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.

# Example
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       	c, w, match = Counter(s1), len(s1), 0

        for i in range(len(s2)):
            if s2[i] in c:
                if not c[s2[i]]: match -= 1
                c[s2[i]] -= 1
                if not c[s2[i]]: match += 1

            if i >= w and s2[i-w] in c:
                if not c[s2[i-w]]: match -= 1
                c[s2[i-w]] += 1
                if not c[s2[i-w]]: match += 1

            if match == len(c):
                return True

        return False
