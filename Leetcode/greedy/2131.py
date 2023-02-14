# 2131. Longest Palindrome by Concatenating Two Letter Words
# Medium

# You are given an array of strings words. Each element of words consists of two lowercase English letters.
#
# Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.
#
# Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.
#
# A palindrome is a string that reads the same forward and backward.

# Example
# Input: words = ["lc","cl","gg"]
# Output: 6
# Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
# Note that "clgglc" is another longest palindrome that can be created.

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        pali = 0
        mid = 0
        side = 0
        counter = collections.Counter(words)
        for word, count in counter.items():
            # if the word is already palidrome
            if word[0] == word[1]:
                # if the two or more palidrome word put on the side
                pali += count // 2 * 2
                # if the palidrome word is odd we can put one in the middle and rest on the side
                if count % 2 != 0:
                    mid = 2
            else:
                # if there is a opposite word put on the side
                side += min(counter[word], counter[word[::-1]])

        return pali * 2 + int(side) * 2 + mid