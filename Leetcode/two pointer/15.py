# 15. 3Sum
# Medium

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.

# Example
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

def threeSum(nums):
    nums.sort()
    result = set()

    for i in range(len(nums)-2):
        l, r = i + 1, len(nums) - 1
        while l < r:
            addup = nums[i] + nums[l] + nums[r]

            if addup < 0:
                l += 1
            elif addup > 0:
                r -= 1

            else:
                result.add(tuple(sorted([nums[i], nums[l], nums[r]])))
                l += 1
                r -= 1

    print(result)

threeSum([-1,0,1,2,-1,-4])