# 40. Combination Sum II
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note: The solution set must not contain duplicate combinations.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(csum: int, index: int, path: List[int]) -> None:
            if csum < 0:
                return

            if csum == 0:
                result.append(path)
                return

            for i in range(index, len(candidates)):
                if index < i and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break

                dfs(csum - candidates[i], i + 1, path + [candidates[i]])

        if sum(candidates) < target:
            return []

        candidates.sort()
        dfs(target, 0, [])
        return result