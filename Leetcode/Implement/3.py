3. Longest Substring Without Repeating Characters
# Medium

# Given a string s, find the length of the longest substring without repeating characters.

#Example
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start = max_len = 0

        for i, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_len = max(max_len, i - start + 1)
            used[char] = i
        return max_len
