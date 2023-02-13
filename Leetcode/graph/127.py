# 127. Word Ladder
# Hard

# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

# Example
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = collections.deque()
        q.append((beginWord, 1))
        visited = {beginWord}

        length = len(beginWord)

        dictionary = collections.defaultdict(list)
        # the words only differ by 1 so add all the possible mutation into the dict
        for word in wordList:
            for i in range(length):
                dictionary[word[:i] + '?' + word[i+1:]].append(word)

        while q:
            cur, step = q.popleft()
            for i in range(length):
                for n in dictionary[cur[:i] + '?' + cur[i+1:]]:
                    if n == endWord:
                        return step + 1
                    if n not in visited:
                        q.append((n, step + 1))
                        visited.add(n)
        return 0