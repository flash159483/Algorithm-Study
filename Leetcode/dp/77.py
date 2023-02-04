# 77. Combinations
# Medium

# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
#
# You may return the answer in any order.

# Example
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(path, start, k):
            if k == 0:
                result.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)
                dfs(path, i + 1, k - 1)
                path.pop()

        dfs([], 1, k)

        return result