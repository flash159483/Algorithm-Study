# 1657. Determine if Two Strings Are Close
# Medium

# Two strings are considered close if you can attain one from the other using the following operations:
#
# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.
#
# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

# Example
# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # length is different or character in word1 and word2 are different
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False

        w1_counter = collections.Counter(word1)
        w2_counter = collections.Counter(word2)

        if w1_counter == w2_counter:
            return True

        seen = set()

        for i in w1_counter.values():
            flag = False
            for w2, j in w2_counter.items():
                # make sure the same word in not used again
                if i == j and w2 not in seen:
                    flag = True
                    seen.add(w2)
                    break
            if not flag:
                return False

        return True

    # def closeStrings(self, w1, w2):
    #     return set(w1) == set(w2) and Counter(Counter(w1).values()) == Counter(Counter(w2).values())

