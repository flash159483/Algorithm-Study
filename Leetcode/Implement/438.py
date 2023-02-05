# 438. Find All Anagrams in a String
# Medium
#
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = len(p)
        pCounter = Counter(p)
        sCounter = Counter(s[:window-1])
        result = []

        for i in range(window-1, len(s)):
            sCounter[s[i]] += 1
            if sCounter == pCounter:
                result.append(i-window+1)
            sCounter[s[i-window+1]] -= 1
            if sCounter[s[i-window+1]] == 0:
                del sCounter[s[i-window+1]]

        return result
