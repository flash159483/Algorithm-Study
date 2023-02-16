# 238. Product of Array Except Self
# Medium

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prev = post = 1
        # multiply all numbers on the leftside of itself
        for i in range(len(nums)):
            result[i] = prev
            prev *= nums[i]

        # multiply all numbers on the rightside of itself
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= post
            post *= nums[i]

        return result
