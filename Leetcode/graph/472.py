# 472. Concatenated Words
# Hard

# Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.
#
# A concatenated word is defined as a string that is comprised entirely of at least two shorter words (not necesssarily distinct) in the given array.

# Example
# Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = set(words)
        visited = {}

        def dfs(word):
            if word in visited:
                return visited[word]

            visited[word] = False

            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in d and suffix in d:
                    visited[word] = True
                    break

                if prefix in d and dfs(suffix):
                    visited[word] = True
                    break

            return visited[word]

        return [word for word in words if dfs(word)]
