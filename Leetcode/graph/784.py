# 784. Letter Case Permutation
# Medium

# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
#
# Return a list of all possible strings we could create. Return the output in any order.


# Example
# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []

        def dfs(letter, i):
            if len(letter) == len(s):
                result.append(letter)
                return

            if s[i].isalpha():
                dfs(letter + s[i].swapcase(), i + 1)

            dfs(letter + s[i], i + 1)

        dfs("", 0)

        return result