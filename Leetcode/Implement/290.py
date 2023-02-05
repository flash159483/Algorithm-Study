# 290. Word Pattern
# easy

# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.


# Example
#input              output
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(set(pattern)) != len(set(s.split())):
            return False
        if len(pattern) != len(s.split()):
            return False

        word, table = s.split(), collections.defaultdict(list)

        for i in range(len(pattern)):
            if pattern[i] not in table:
                table[pattern[i]] = word[i]
            if table[pattern[i]] != word[i]:
                return False
        return True