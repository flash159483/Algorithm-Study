# 433. Minimum Genetic Mutation
# Medium

# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.
#
# Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.
#
# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.
#
# Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.
#
# Note that the starting point is assumed to be valid, so it might not be included in the bank.

# Example
# Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def check(a, b):
            return sum([1 for i in range(len(a)) if a[i] != b[i]]) == 1
        q = collections.deque()

        q.append((startGene, 0))
        visited = {startGene}

        while q:
            cur, step = q.popleft()
            if cur == endGene:
                return step

            for i in bank:
                if check(i, cur) and i not in visited:
                    q.append((i, step+1))
                    visited.add(i)
        return -1
