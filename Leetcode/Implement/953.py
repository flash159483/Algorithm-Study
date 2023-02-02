#953. Verifying an Alien Dictionary
# Easy

# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

#Example
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def compare(w1, w2):
            for a, b in zip(w1, w2):
                if a != b:
                    return d[a] < d[b]

            return len(w1) <= len(w2)

        d = {order[i]: i for i in range(len(order))}

        return all(compare(words[i - 1], words[i]) for i in range(1, len(words)))

