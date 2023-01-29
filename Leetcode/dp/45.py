# 45. Jump Game II
#Medium
#
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
#
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

#Example
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

class Solution:
    def jump(self, nums: int, pos = 0) -> int:
        # the initial range (after 0th jump) is [0,0]
        cur = jump_pos = 0
        nJumps = 0
        while jump_pos < len(nums) - 1:
            nJumps += 1
            furthest = max([i + nums[i] for i in range(cur,jump_pos+1)])
            cur, jump_pos = jump_pos + 1, furthest

        return nJumps