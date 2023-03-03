# 28. Find the Index of the First Occurrence in a String
# Medium

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        n = len(needle)
        first = collections.deque(haystack[:n - 1])

        for i in range(n - 1, len(haystack)):
            first.append(haystack[i])
            if needle == ''.join(first):
                return i - n + 1
            first.popleft()

        return -1


