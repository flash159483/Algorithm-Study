# 47. Permutations II
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in
# any order.

#Example
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()
        prev_element = []

        def dfs(element):
            if len(element) == 0:
                result.add(tuple(prev_element[:]))

            for e in element:
                next_element = element[:]
                next_element.remove(e)
                prev_element.append(e)
                dfs(next_element)
                prev_element.pop()

        dfs(nums)
        return result