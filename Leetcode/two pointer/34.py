#34 Find First and Last Position of Element in Sorted Array
# Medium

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.

# Example
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchLeft():
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left += 1
                else:
                    right -= 1
            return left

        def searchRight():
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] <= target:
                    left += 1
                else:
                    right -= 1
            return right

        left, right = searchLeft(), searchRight()

        return (left, right) if left <= right else (-1, -1)
