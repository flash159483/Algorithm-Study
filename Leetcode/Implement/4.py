# 4. Median of Two Sorted Arrays
# Hard

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).

# Example
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        result = 0
        if len(nums1) % 2 == 0:
            mid = int(len(nums1) / 2)
            result = (nums1[mid] + nums1[mid-1]) /2
        else:
            mid = int(len(nums1) / 2)
            result = nums1[mid]
        return result
