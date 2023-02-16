# 451. Sort Characters By Frequency
# Medium

# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
#
# Return the sorted string. If there are multiple answers, return any of them.


# Example
# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.


class Solution:
    def frequencySort(self, s: str) -> str:
        c = collections.Counter(s)
        result = ''

        for i in c.most_common(len(s)):
            for _ in range(i[1]):
                result += i[0]

        return result