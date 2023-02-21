# 540. Single Element in a Sorted Array
# Medium

# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
#
# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

# example
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = 2 * ((l + r) // 4)

            # if the target num is in the right side all the num in the left side is even
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid

        return nums[l]