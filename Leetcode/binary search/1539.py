# 1539. Kth Missing Positive Number
# Easy

# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
#
# Return the kth positive integer that is missing from this array.

# Example
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            if arr[mid] - mid > k:
                r = mid
            else:
                l = mid + 1
        return r + k