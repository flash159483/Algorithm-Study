# 46. Permutations
# Medium

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_element = []

        def dfs(element):
            if len(element) == 0:
                result.append(prev_element[:])

            for e in element:
                next_element = element[:]
                next_element.remove(e)
                prev_element.append(e)
                dfs(next_element)
                prev_element.pop()

        dfs(nums)
        return result