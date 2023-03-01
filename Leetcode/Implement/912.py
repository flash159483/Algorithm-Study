# 912. Sort an Array
# Medium

# Given an array of integers nums, sort the array in ascending order and return it.
#
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.


# Example
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        if len(arr) > 1:
            mid = len(arr) // 2
            l = arr[:mid]
            r = arr[mid:]

            self.sortArray(l)
            self.sortArray(r)

            i, j, k = 0, 0, 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    arr[k] = l[i]
                    i += 1
                    k += 1
                else:
                    arr[k] = r[j]
                    j += 1
                    k += 1

            while i < len(l):
                arr[k] = l[i]
                i += 1
                k += 1
            while j < len(r):
                arr[k] = r[j]
                j += 1
                k += 1
        return arr